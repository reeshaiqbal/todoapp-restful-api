from django.db import models
from accounts.models import CustomUserModel   # builtin django User model

# Create your models here.


class Todo(models.Model):
    user = models.ForeignKey(
        CustomUserModel, on_delete=models.CASCADE, related_name='viewset_todos')
    title = models.CharField(max_length=300)
    done = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
