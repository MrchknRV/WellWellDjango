from django.urls import path
from . import views

app_name = "catalog"

urlpatterns = [
    path('product/list', views.ProductListView.as_view(), name='product_list'),
    path('contacts/', views.ContactsTemplateView.as_view(), name='contacts'),
    path('product/detail/<int:pk>/', views.ProductDetailView.as_view(), name="product_detail")
]
