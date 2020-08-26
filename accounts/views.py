from django.views.generic import CreateView
from django.urls import reverse_lazy

from .forms import SignUpForm


class UserSignUpView(CreateView):
	form_class = SignUpForm
	success_url = reverse_lazy('login')
	template_name = 'accounts/signup.html'

