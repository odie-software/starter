from django.contrib.auth.models import AbstractUser
from django.db import models


class RoleChoices(models.IntegerChoices):
    ADMIN = 0
    USER = 1


class CustomUser(AbstractUser):
    role = models.PositiveSmallIntegerField(
        choices=RoleChoices.choices, default=RoleChoices.USER
    )
