from django.urls import path
from . import views

app_name = "catalog"

urlpatterns = [
    path("product/list", views.ProductListView.as_view(), name="product_list"),
    path("contacts/", views.ContactsTemplateView.as_view(), name="contacts"),
    path("product/detail/<int:pk>/", views.ProductDetailView.as_view(), name="product_detail"),
    path("product/create/", views.ProductCreateView.as_view(), name="product_create"),
    path("product/update/<int:pk>/", views.ProductUpdateView.as_view(), name="product_update"),
    path("product/delete/<int:pk>/", views.ProductDeleteView.as_view(), name="product_delete"),
    path("category/", views.CategoryListView.as_view(), name="category_list"),
    path("category/create/", views.CategoryCreateView.as_view(), name="category_create"),
]
