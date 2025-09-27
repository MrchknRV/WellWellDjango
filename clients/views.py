from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView

from config.settings import EMAIL_HOST_USER
from .forms import ClientCreationForm
from django.core.mail import send_mail
from django.contrib.auth import login


class RegisterView(CreateView):
    form_class = ClientCreationForm
    template_name = "auth/client/register.html"
    success_url = reverse_lazy("catalog:product_list")

    def form_valid(self, form):
        user = form.save()
        user_name = form.cleaned_data.get("first_name")
        user_email = form.cleaned_data.get("email")
        login(self.request, user)
        self._send_welcome_email(user_name, user_email)
        return super().form_valid(form)

    def _send_welcome_email(self, user_name, user_email):
        subject = f"Здравствуйте! {user_name.title()}, добро пожаловать на наш сервис"
        message = f"Благодарим Вас за регистрацию"
        recipient_list = [user_email]
        from_email = EMAIL_HOST_USER
        send_mail(subject, message, from_email, recipient_list)


class ClientLoginView(LoginView):
    template_name = "auth/client/login.html"
    reverse_lazy = reverse_lazy("catalog:product_list")


class ClientLogoutView(LogoutView):
    next_page = reverse_lazy("catalog:product_list")
