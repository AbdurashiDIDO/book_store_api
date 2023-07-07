from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from apps.models.books import Book


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        depth = 1
        fields = '__all__'
