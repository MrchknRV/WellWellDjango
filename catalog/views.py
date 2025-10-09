from django.urls import reverse_lazy, reverse
from catalog.models import Product, Category
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.contrib import messages
from .forms import CategoryForm, ContactForm, ProductCreateForm


class ContactsTemplateView(FormView):
    form_class = ContactForm
    template_name = "catalog/contacts.html"
    success_url = reverse_lazy("catalog:contacts")


class ProductListView(ListView):
    model = Product
    template_name = "catalog/product/product_list.html"
    context_object_name = "products"

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            if self.request.user.has_perm("catalog.can_delete_product"):
                return queryset
            return queryset.filter(owner=self.request.user)
        return queryset.none()


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = "catalog/product/product_detail.html"
    context_object_name = "product"
    login_url = reverse_lazy("clients:login")


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductCreateForm
    template_name = "catalog/product/product_form.html"
    success_url = reverse_lazy("catalog:product_list")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['owner'] = self.request.user
        return kwargs

    def form_valid(self, form):
        messages.success(self.request, "Продукт успешно создан")
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductCreateForm
    template_name = "catalog/product/product_form.html"

    def get_success_url(self):
        return reverse("catalog:product_detail", args=[self.kwargs.get("pk")])

    def form_valid(self, form):
        messages.success(self.request, "Продукт успешно создан")
        return super().form_valid(form)

    def get_object(self):
        obj = self.get_object()
        return obj.owner == self.request.user

class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Product
    permission_required = ['catalog.can_delete_product', "catalog.can_unpublish_product"]
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
