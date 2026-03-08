from django.contrib.auth.models import AbstractUser
from django.db import models

from api.roles.models import Role


class User(AbstractUser):
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.username
