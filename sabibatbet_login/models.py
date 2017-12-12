from django.db import models

# Create your models here.
class User(models.Model):
    id = models.CharField('id', max_length=20, primary_key=True, )
    name = models.CharField('Name', max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
