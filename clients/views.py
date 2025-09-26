from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from .forms import ClientCreationForm


class RegisterView(CreateView):
    form_class = ClientCreationForm
    template_name = "auth/client/register.html"
    reverse_lazy = reverse_lazy("catalog:product_list")


class ClientLoginView(LoginView):
    template_name = "auth/client/login.html"
    reverse_lazy = reverse_lazy("catalog:product_list")


class ClientLogoutView(LogoutView):
    next_page = reverse_lazy("catalog:product_list")
