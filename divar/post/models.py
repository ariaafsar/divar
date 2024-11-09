from django.db import models
from user.models import Account
class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(Account, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    create_time = models.DateTimeField(auto_now_add=True)

# Create your models here.
