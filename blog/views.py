from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from .models import Post


class PostModelCreate(CreateView):
    model = Post
    fields = ["title", "body", "image", "status", "is_active"]
    template_name = 'blog/post/post_form.html'
    success_url = reverse_lazy("blog:post_list")


class PostModelUpdateView(UpdateView):
    model = Post
    fields = ["title", "body", "image", "status"]
    template_name = 'blog/post/post_form.html'

    def get_success_url(self):
        return reverse("blog:post_detail", args=[self.kwargs.get("pk")])


class PostModelListView(ListView):
    model = Post
    template_name = "blog/post/post_list.html"
    context_object_name = "posts"

    def get_queryset(self):
        return Post.objects.filter(is_active=True)


class PostModelDetailView(DetailView):
    model = Post
    template_name = "blog/post/post_detail.html"
    context_object_name = "post"

    def get_object(self, queryset=None):
        post = super().get_object()
        post.views_count += 1
        post.save()
        return post


class PostModelDeleteView(DeleteView):
    model = Post
    template_name = "blog/post/post_delete_confirm.html"
    success_url = reverse_lazy("blog:post_list")
