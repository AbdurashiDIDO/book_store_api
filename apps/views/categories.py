from rest_framework.viewsets import ModelViewSet

from apps.models.categories import Category
from apps.serializers.books import BookSerializer


class CategoryModelViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = BookSerializer
