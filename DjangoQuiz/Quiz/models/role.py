from django.db import models


class Role(models.Model):
    ROLES = (
        ('Student', 'Student'),
        ('Teacher', 'Teacher'),
    )
    role = models.CharField(max_length=7, choices=ROLES)

    def __str__(self):
        return self.role
