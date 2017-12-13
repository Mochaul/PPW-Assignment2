from django.db import models
# # Create your models here.
class Post(models.Model):
    company_id = models.CharField('Company ID', max_length=200)
    content = models.TextField('Content', max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
