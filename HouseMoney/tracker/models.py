from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Payment(models.Model):
    name = models.TextField(max_length=15)
    notes = models.TextField(max_length=200)
    value = models.DecimalField(max_digits=5, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    proof = models.ImageField()


class Log(models.Model):
    choices = [
        ('E', 'Electric'),
        ('G', 'Gas')
    ]
    time = models.DateTimeField(auto_now_add=True)
    value = models.DecimalField(max_digits=5, decimal_places=2)
    utility = models.CharField(choices=choices, max_length=1)
    logger = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
