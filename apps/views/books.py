from PyPDF2 import PdfReader
from rest_framework.viewsets import ModelViewSet

from apps.models.books import Book
from apps.serializers.books import BookSerializer


class BookModelViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def create(self, request, *args, **kwargs):
        pdf = request.FILES['content']
        render = PdfReader(pdf)

        book = Book(
            title=request.data['title'],
            content=pdf,
            category_id=request.data['category_id'],
            year=request.data['year']
        )

        book.pages = len(render.pages)

        book.save()
        # return super().create(request, *args, **kwargs)
