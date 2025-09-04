from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'category_name']
    search_fields = ['category_description', 'category_name']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'product_name', 'product_price', 'category']
    list_filter = ['category', 'created_at']
    search_fields = ['product_name', 'product_description']
    raw_id_fields = ['category']
