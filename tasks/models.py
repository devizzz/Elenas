from django.db import models
from users.models import User

# django-ckeditor
from ckeditor.fields import RichTextField

class Task(models.Model):
    """Task model."""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = RichTextField(max_length=250)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    state = models.BooleanField(default=False)

    def __str__(self):
        """Return task title and first_name and last_name."""
        return f'{self.user.first_name} {self.user.last_name} | {self.title}'