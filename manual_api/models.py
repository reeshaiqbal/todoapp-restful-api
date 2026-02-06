from django.db import models
from accounts.models import CustomUserModel   # builtin django User model


# Create your models here.


# Inheriting from models.Model makes "Todo" a Django model class. Then Django maps it to a Database table (attributes to columns and instances to rows).
class Todo(models.Model):
    # user_id is stored in user, and is a foreign key from User table which acts as a bridge b/w Todo and authtoken_token table to authenticat,authorize and fetch todos related to the user only
    user = models.ForeignKey(
        CustomUserModel, on_delete=models.CASCADE, related_name='manual_todos')
    title = models.TextField(max_length=300)
    done = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
