from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, FormView, ListView, UpdateView

from catalog.models import Category, Product, Status

from .forms import CategoryForm, ContactForm, ProductCreateForm
from .mixins import OwnerOrModeratorMixins, OwnerRequiredMixin, ProductOwnerQuerysetMixin

from django.core.cache import cache
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

from .service import ProductListService


class ContactsTemplateView(FormView):
    form_class = ContactForm
    template_name = "catalog/contacts.html"
    success_url = reverse_lazy("catalog:contacts")


class ProductListView(ProductOwnerQuerysetMixin, ListView):
    model = Product
    template_name = "catalog/product/product_list.html"
    context_object_name = "products"

    def get_queryset(self):
        queryset = cache.get("products_queryset")
        if not queryset:
            queryset = super().get_queryset()
            cache.set("products_queryset", queryset, 60 * 10)
        category_id = ProductListService.get_category_id(self.request)
        if category_id:
            queryset = queryset.filter(category_id=category_id)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ProductListService.get_categories()
        context['selected_category'] = ProductListService.get_selected_categories(self.request)
        return context


@method_decorator(cache_page(60 * 10), name="dispatch")
class ProductDetailView(OwnerOrModeratorMixins, LoginRequiredMixin, DetailView):
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
        kwargs["user"] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.owner = self.request.user
        messages.success(self.request, "Продукт успешно создан")
        return super().form_valid(form)


class ProductUpdateView(OwnerRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductCreateForm
    template_name = "catalog/product/product_form.html"

    def get_success_url(self):
        return reverse("catalog:product_detail", args=[self.kwargs.get("pk")])

    def form_valid(self, form):
        messages.success(self.request, "Продукт успешно обновлен")
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs


class ProductDeleteView(OwnerOrModeratorMixins, LoginRequiredMixin, DeleteView):
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


@login_required
def unpublish_product(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if product.owner != request.user and not request.user.has_perm("catalog.can_unpublish_product"):
        raise PermissionDenied("У вас нет прав для отмены публикации этого продукта")

    product.status = Status.DRAFT
    product.save()
    messages.success(request, "Публикация продукта отменена.")
    return redirect("catalog:product_detail", pk=product.pk)


@login_required
def publish_product(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if product.owner != request.user and not request.user.has_perm("catalog.can_publish_product"):
        raise PermissionDenied("У вас нет прав для публикации этого продукта")

    if product.status == Status.DRAFT:
        product.status = Status.PUBLISHED
        product.save()
        messages.success(request, "Продукт успешно опубликован!")
    else:
        messages.warning(request, "Продукт уже опубликован.")

    return redirect("catalog:product_detail", pk=product.pk)
