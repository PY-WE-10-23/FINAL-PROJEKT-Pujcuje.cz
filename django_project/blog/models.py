from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image

class Category(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    content = models.TextField()
    image = models.ImageField(default='default_item.jpg', upload_to='item_pics')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

    def save(self, **kwargs):
        super(Item, self).save(**kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class XYZ_TestData(models.Model):
   my_title = models.CharField('XYZ Title',max_length=255)
   my_date= models.DateField('XYZ Date')
   my_date_time = models.DateTimeField('XYZ DateTime')
   my_active = models.BooleanField(default=True)
   my_des = models.TextField('XYZ Description',default='Test')