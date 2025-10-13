from django.contrib.auth.mixins import UserPassesTestMixin


class OwnerRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        product = self.get_object()
        return product.owner == self.request.user


class ProductOwnerQuerysetMixin:

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            if self.request.user.has_perm("catalog.can_delete_product"):
                return queryset
            return queryset.filter(owner=self.request.user)
        return queryset.none()


class OwnerOrModeratorMixins(UserPassesTestMixin):
    def test_func(self):
        product = self.get_object()
        user = self.request.user

        if product.owner == user:
            return True

        return user.has_perm("catalog.can_delete_product")
