from django.db import models

# Create your models here.


# Inheriting from models.Model makes "Todo" a Django model class. Then Django maps it to a Database table (attributes to columns and instances to rows).
class Todo(models.Model):

    title = models.TextField(max_length=300)
    done = models.BooleanField(default=False)
