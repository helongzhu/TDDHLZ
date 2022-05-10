from cgitb import text
from django.db import models


# Create your models here.
class Item(models.Model):
    text = models.TextField(default='')