from .models import Category

class ProductListService:

    # @staticmethod
    # def get_filtered_queryset(queryset,request):
    #     category_id = request.GET.get("category")
    #     if category_id:
    #         queryset = queryset.filter(category_id=category_id)
    #     return queryset

    @staticmethod
    def get_category_id(request):
        return request.GET.get("category")


    @staticmethod
    def get_categories():
        return Category.objects.all()

    @staticmethod
    def get_selected_categories(request):
        return request.GET.get('category', '')
