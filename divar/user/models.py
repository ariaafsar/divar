from django.db import models
from django.contrib.auth.models import User
from post.models import Post
class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=11)
    email = models.EmailField(max_length=255)
    published_posts = models.ForeignKey(Post , on_delete=models.CASCADE)

# Create your models here.
