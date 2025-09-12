from django.urls import path
from . import views

app_name = "catalog"

urlpatterns = [
    path('home/', views.product_list, name='home'),
    path('contacts/', views.contacts, name='contacts'),
    path('<int:id>/', views.product_detail, name="product_detail")
]
