from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=100, verbose_name='категория')
    category_description = models.TextField()

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ['category_name']


class Product(models.Model):
    product_name = models.CharField(max_length=150, verbose_name='продукт')
    product_description = models.TextField()
    product_image = models.ImageField(upload_to='photos/', verbose_name='фотография')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    product_price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ['-created_at']
