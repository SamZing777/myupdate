import threading

from django.contrib import admin
from django.contrib.auth.models import Group
from django_admin_lightweight_date_hierarchy.admin import RangeBasedDateHierarchyListFilter
from django.utils.safestring import mark_safe
from django.conf  import settings
from django.http import HttpResponse
from django.utils.datastructures import MultiValueDictKeyError
from django.core.mail import (
	send_mail,
	BadHeaderError,
	EmailMessage
)

from .models import User, BroadcastEmail


class EmailThreading(threading.Thread):
	def __init__(self, subject, html_content, recipient_list):
		self.subject = subject
		self.recipient_list = recipient_list
		self.html_content = html_content
		threading.Thread.__init__(self)

	def run(self):
		msg = EmailMessage(self.subject, self.html_content, settings.EMAIL_HOST_USER, self.recipient_list)
		msg.content_subtype = 'html'

		try:
			msg.send()
		except BadHeaderError:
			return HttpResponse('Invalid header found.')

	

class BroadcastEmailAdmin(admin.ModelAdmin):
	broadcast = BroadcastEmail
	actions = ['submit_email']
	list_display = ('subject', 'timeStamp')
	search_fields = ['subject']

	def submit_email(self, request, obj):
		list_email_user = [p.email for p in User.objects.all()]

		obj_selected = obj[0]
		EmailThreading(obj_selected.subject, mark_safe(obj_selected.body),
					   list_email_user).start()

		return HttpResponse('<h2 style="color:green;">'
				'Broadcast Email successfully sent to all Users.</h2>')

	submit_email.short_description = 'Send broadcast email'
	submit_email.allow_tags = True


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
	date_hierarchy = 'date_joined'
	# change_list_template = 'admin/users_changelist.html'
	actions = ['setInactive']
	list_display = ['username', 'email', 'is_active', 'is_staff', 'date_joined']
	list_filters = (
		RangeBasedDateHierarchyListFilter,
	)

	def setInactive(self, request, user=None):
		# does nothing (considering change_list.html)
		try:
			user = User.objects.get(request.POST['user.id'])
			user.is_active = False
			user.save()
		except MultiValueDictKeyError:
			request.user.is_active = False
			return user

		# flags current staff user as inactive
		'''
		user = request.POST.get('user.id')
		request.user.is_active = False
		request.user.save()
		return HttpResponse('<h2 style="color:green;">'
			                'User has been flagged as inactive.</h2>')
		'''
		

	setInactive.short_description = 'Make inactive'


admin.site.register(BroadcastEmail, BroadcastEmailAdmin)
admin.site.unregister(Group)
