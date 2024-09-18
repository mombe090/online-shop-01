from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView, BaseDetailView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.conf import settings
from django.contrib import messages
from django.db import transaction

from .forms import CustomAuthenticationForm
from .forms import CustomUserCreationForm


class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm


class CustomUserCreationView(CreateView):
    template_name = 'registration/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('register')

    def form_valid(self, form):
        with transaction.atomic():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            self.send_activation_email(user)
        return redirect(self.success_url)

    def send_activation_email(self, user):
        subject = "Activation de votre compte"
        token = urlsafe_base64_encode(force_bytes(user.pk))
        message = render_to_string(
            'registration/activation_email.html', {
                'user': user,
                'token': token,
                'domain': settings.DOMAIN_URL
            }
        )
        messages.success(
            self.request,
            ("Votre compte compte a ete cree, consulter "
                "votre boite email pour activer votre compte")
        )
        send_mail(
            subject, message,
            'backend@nimbasms.com',
            [user.email],
            fail_silently=True
        )


class ActivationUserView(BaseDetailView):
    template_name = 'registration/confirm_user_activation.html'
