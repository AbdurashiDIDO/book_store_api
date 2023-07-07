from rest_framework.viewsets import ModelViewSet

from apps.models.authors import Author
from apps.serializers.books import BookSerializer


class AuthorModelViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = BookSerializer
