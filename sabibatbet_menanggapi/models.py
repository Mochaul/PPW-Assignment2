from django.db import models
from sabibatbet_forum.models import Post
# Create your models here.
class Tanggapan(models.Model):
    post_id = models.ForeignKey(Post, null=True)
    name = models.CharField('Name', max_length=200)
    content = models.TextField('Content', max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
