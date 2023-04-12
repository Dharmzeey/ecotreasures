from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
  first_name = models.CharField(max_length=150, null=False)
  last_name = models.CharField(max_length=150, null=False)
  email = models.EmailField(unique=True)
  is_seller = models.BooleanField(default=False)

  def __str__(self):
    return self.username

class Seller(models.Model):
  user = models.OneToOneField(User, on_delete=models.SET_NULL, related_name="user_seller", null=True)
  def __str__(self):
    return self.user.username