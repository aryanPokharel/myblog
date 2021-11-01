from django.db import models
from datetime import datetime

# Create your models here.
class Article(models.Model):
    name = models.CharField(max_length=100, null=False)
    category = models.CharField(default='Random', null=True, max_length=100)
    image = models.FileField(null=True, upload_to='static/uploads')
    text = models.TextField(max_length=4000, null=True)



