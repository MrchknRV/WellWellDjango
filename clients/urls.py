from django.urls import path

from . import views

app_name = "clients"

urlpatterns = [
    path("register/", views.RegisterView.as_view(), name="register"),
    path("login/", views.ClientLoginView.as_view(), name="login"),
    path("logout/", views.ClientLogoutView.as_view(), name="logout"),
]
