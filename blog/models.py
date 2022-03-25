from django.db import models

# Create your models here.

class post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    # tags = models.TextField
    # author = models.TextField
    counted_view = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.BooleanField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

