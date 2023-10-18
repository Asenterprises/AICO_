from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    USER_TYPE_CHOICES = (
        (1, 'production'),
        (2, 'quality'),
        (3, 'warehouse'),
    )

    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username