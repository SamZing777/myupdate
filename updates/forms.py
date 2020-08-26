from django import forms

from .models import Update
from accounts.models import BroadcastEmail


class UpdateForm(forms.ModelForm):
	class Meta:
		model = Update
		fields = ['topic', 'matter', 'description', 'area']

		def save(self, user=None):
			update = super(UpdateForm, self).save(commit=False)
			if user:
				update.informant = user
			update.save()
			return update


class BroadcastEmailForm(forms.ModelForm):
	class Meta:
		model = BroadcastEmail
		fields = ['subject', 'body']

	def save(self, user=None):
		email = super(BroadcastEmailForm, self).save(commit=False)
		if user:
			email.user = user
		email.save()
		return email
