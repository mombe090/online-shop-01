from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView

from .forms import CustomAuthenticationForm
from .forms import CustomUserCreationForm


class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm


class CustomUserCreationView(CreateView):
    template_name = 'registration/register.html'
    form_class = CustomUserCreationForm
