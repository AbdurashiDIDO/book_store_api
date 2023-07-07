from django.urls import include, path
from rest_framework.routers import SimpleRouter

from apps.views.author import AuthorModelViewSet
from apps.views.books import BookModelViewSet
from apps.views.categories import CategoryModelViewSet

router = SimpleRouter()
router.register(r'books', BookModelViewSet)
router.register(r'authors', AuthorModelViewSet)
router.register(r'categories', CategoryModelViewSet)

urlpatterns = [
    path('', include(router.urls)),

]
