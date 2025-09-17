from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path('', views.PostModelListView.as_view(), name="post_list"),
    path('post/create/', views.PostModelCreate.as_view(), name="post_create"),
    path('post/detail/<int:pk>/', views.PostModelDetailView.as_view(), name="post_detail"),
    path('post/<int:pk>/update/', views.PostModelUpdateView.as_view(), name="post_update"),
    path('post/<int:pk>/delete/', views.PostModelDeleteView.as_view(), name="post_delete"),
]
