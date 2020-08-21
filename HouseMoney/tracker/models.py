from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Payment(models.Model):
    name = models.TextField(max_length=15)
    notes = models.TextField(max_length=200)
    value = models.DecimalField(max_digits=5, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    proof = models.ImageField()
