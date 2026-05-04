from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('accounts', 'Accounts'),
        ('hr', 'HR'),
        ('project', 'Project Management'),
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    
    