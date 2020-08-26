from django.views import generic
from django.urls import reverse_lazy

from .models import Update
from .forms import UpdateForm, BroadcastEmailForm


class HomePageView(generic.ListView):
	model = Update
	context_object_name = 'updates'
	paginate_by = 10
	template_name = 'updates/index.html'


class UserCreateUpdateView(generic.CreateView):
	form_class = UpdateForm
	success_url = reverse_lazy('index')
	template_name = 'updates/create_update.html'

	def form_valid(self, form):
		form.instance.informant = self.request.user
		return super().form_valid(form)


class UpdateDetailView(generic.DetailView):
	model = Update
	template_name = 'updates/update_detail.html'


class StaffBroadCastEmailView(generic.CreateView):
	form_class = BroadcastEmailForm
	success_url = reverse_lazy('index')
	template_name = 'updates/email_users.html'

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)


class Savest(generic.TemplateView):
	template_name = 'updates/savest.html'
