"""Task URLs."""

# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from . import views

router = DefaultRouter()
router.register("task", views.TaskViewSet, basename='task')

urlpatterns = [
    path('', include(router.urls))
]