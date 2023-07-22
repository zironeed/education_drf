from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

NULLABLE = {'null': True, 'blank': True}


class UserRoles(models.TextChoices):
    MEMBER = 'member', _('member')
    MODERATOR = 'moderator', _('moderator')


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='Email')
    phone = models.CharField(max_length=30, verbose_name='Phone', **NULLABLE)
    city = models.CharField(max_length=100, verbose_name='City', **NULLABLE)
    avatar = models.ImageField(upload_to='User_avatar', **NULLABLE)
    role = models.CharField(max_length=9, choices=UserRoles.choices, default=UserRoles.MEMBER, verbose_name='Role')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
