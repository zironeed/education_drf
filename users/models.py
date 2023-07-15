from django.db import models
from django.contrib.auth.models import AbstractUser

NULLABLE = {'null': True, 'blank': True}


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='Email')
    phone = models.CharField(max_length=30, verbose_name='Phone', **NULLABLE)
    city = models.CharField(max_length=100, verbose_name='City', **NULLABLE)
    avatar = models.ImageField(upload_to='User_avatar', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
