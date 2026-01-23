from django.db import models

# Create your models here.


class Todo(models.Model):
    title = models.TextField(max_length=300)
    done = models.BooleanField(default=False)
