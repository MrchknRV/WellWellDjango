from django.urls import reverse_lazy, reverse
from catalog.models import Product, Category
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from .forms import ProductForm, CategoryForm, ContactForm


class ContactsTemplateView(FormView):
    form_class = ContactForm
    template_name = "catalog/contacts.html"
    success_url = reverse_lazy("catalog:contacts")


class ProductListView(ListView):
    model = Product
    template_name = "catalog/product/product_list.html"
    context_object_name = "products"


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = "catalog/product/product_detail.html"
    context_object_name = "product"
    login_url = reverse_lazy("clients:login")


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product/product_form.html"
    success_url = reverse_lazy("catalog:product_list")


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product/product_form.html"

    def get_success_url(self):
        return reverse("catalog:product_detail", args=[self.kwargs.get("pk")])


class ProductDeleteView(DeleteView):
    model = Product
    template_name = "catalog/product/product_delete_confirm.html"
    success_url = reverse_lazy("catalog:product_list")


class CategoryListView(ListView):
    model = Category
    template_name = "catalog/category/category_list.html"
    context_object_name = "categories"


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = "catalog/category/category_create.html"
    success_url = reverse_lazy("catalog:category_list")
