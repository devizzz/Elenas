# Django REST Framework
from rest_framework import mixins, status, viewsets
from rest_framework.response import Response

# Permissions
from rest_framework.permissions import IsAuthenticated
from users.permissions import HasPermission

#Serializers
from tasks.serializers import (TaskModelSerializer, TaskSerializer)

#Model 
from tasks.models import Task

class TaskViewSet(mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        viewsets.GenericViewSet):

    serializer_class = TaskModelSerializer

    def get_permissions(self):
        permission_classes = [IsAuthenticated, HasPermission]
        return [permission() for permission in permission_classes]

    def create(self, request, *args, **kwargs):
        serializer = TaskSerializer(data=request.data, context={"request": self.request})
        serializer.is_valid(raise_exception=True)
        task = serializer.save()
        data = TaskModelSerializer(task).data
        return Response(data, status=status.HTTP_201_CREATED)

    def get_queryset(self):
        """Restrict list to only user experience."""
        queryset = Task.objects.filter(user=self.request.user)
        return queryset