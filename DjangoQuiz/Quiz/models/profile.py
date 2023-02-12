from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from Quiz.models.role import Role


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=False, null=False)
    last_name = models.CharField(max_length=255, blank=False, null=False)
    email = models.EmailField(unique=True, blank=False, null=False)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, blank=False, null=False)

    def __str__(self):
        if self.role:
            return f"{self.name} {self.last_name} - {self.role}"
        else:
            return f"{self.name} {self.last_name}"

    def get_absolute_url(self):
        return reverse('index')
