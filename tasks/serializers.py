# Django REST Framework
from rest_framework import serializers
# Model
from .models import Task

class TaskModelSerializer(serializers.ModelSerializer):
    """Task Model Serializer"""

    class Meta:
        """Meta class."""

        model = Task
        fields = (
            'pk',
            'title',
            'description',
            'create_date',
            'update_date',
            'state',
        )

class TaskSerializer(serializers.Serializer):

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    title = serializers.CharField(max_length=50)
    description = serializers.CharField(max_length=250)
    state = serializers.BooleanField(default=False)

    def create(self, data):

        task = Task.objects.create(**data)
        return task