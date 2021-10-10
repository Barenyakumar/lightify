from django.db import models

# Create your models here.
class Helper(models.Model):
    username = models.CharField(max_length=120)
    can_help=models.BooleanField(default=True)

class Blind(models.Model):
    username = models.CharField(max_length=120)
    need_help = models.BooleanField(default=True)
