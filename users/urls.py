"""Users URLs."""

# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from . import views as user_views

router = DefaultRouter()
router.register("users", user_views.UserViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls))
]