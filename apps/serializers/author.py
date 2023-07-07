from rest_framework.serializers import ModelSerializer

from apps.models.authors import Author


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        depth = 1
        fields = '__all__'
