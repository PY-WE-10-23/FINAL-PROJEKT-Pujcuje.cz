from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Category(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    content = models.TextField()
    image = models.ImageField(default='default.jpg', upload_to='item_pics')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title