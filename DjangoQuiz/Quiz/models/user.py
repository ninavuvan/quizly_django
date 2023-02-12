"""

from django.db import models

class Role(models.Model):
    name = models.CharField(max_length=10)


class User(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    last_name = models.CharField(max_length=255, blank=False, null=False)
    username = models.CharField(max_length=255, unique=True, blank=False, null=False)
    password = models.CharField(max_length=255, blank=False, null=False)
    email = models.EmailField(unique=True, blank=False, null=False)
    role = models.OneToOneField(Role, on_delete=models.CASCADE, blank=False, null=False)

    def __str__(self):
        return self.username
"""
