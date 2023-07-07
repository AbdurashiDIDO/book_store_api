from rest_framework.serializers import ModelSerializer

from apps.models.categories import Category


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        depth = 1
        fields = '__all__'
