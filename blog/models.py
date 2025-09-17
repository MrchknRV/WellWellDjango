from django.db import models
from django.utils import timezone

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)

class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = "DR", "Draft"
        PUBLISHED = "PB", "Published"

    title = models.CharField(max_length=150, verbose_name="Заголовок")
    body = models.TextField(verbose_name="Содержание")
    image = models.ImageField(upload_to='photos/blog/', verbose_name='Фотография', blank=True)
    publish_at = models.DateTimeField(default=timezone.now, verbose_name="Дата публикации")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Последнее обновление")
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT, verbose_name="Статус")
    views_count = models.PositiveIntegerField(default=0, verbose_name="Количество просмотров")
    is_active = models.BooleanField(default=True, verbose_name="Статус публикации")
    objects = models.Manager()
    published = PublishedManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "пост"
        verbose_name_plural = "посты"
        ordering = ["-publish_at"]
        indexes = [models.Index(fields=["-publish_at"])]