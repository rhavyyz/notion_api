from django.db import models

# Create your models here.

class Post(models.Model):
    username = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_datetime = models.DateTimeField(auto_now_add=True, blank=True)
    
