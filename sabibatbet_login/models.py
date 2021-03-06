from django.db import models

# Create your models here.
class User(models.Model):
    id = models.CharField('id', max_length=20, primary_key=True, )
    name = models.CharField('Name', max_length=200)
    company = models.CharField('company', max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
