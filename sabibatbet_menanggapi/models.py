from django.db import models

# Create your models here.
class Tanggapan(models.Model):
    name = models.CharField('Name', max_length=200)
    content = models.TextField('Content', max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
