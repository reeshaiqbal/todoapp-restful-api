from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password, **extra_fields):
        user = self.model(username=username, email = email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user    

class CustomUserModel(AbstractUser):   #Inherited from AU, so its attributes & permissions can be used 
    phone_number = models.CharField(max_length=13)
    objects = CustomUserManager()