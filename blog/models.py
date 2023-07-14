from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
# from location_field.models.plain import PlainLocationField

# Create your models here.

'''
   - fields , options
   - validation
   - html widget

'''

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=30000)
    create_date = models.DateTimeField(default=timezone.now())
    draft = models.BooleanField(default=True)
    tags = TaggableManager()
    image = models.ImageField(upload_to='posts')
    auther = models.ForeignKey(User , on_delete=models.SET_NULL, null=True)
    # city = models.CharField(max_length=255)
    # location = PlainLocationField(based_fields=['egypt'], zoom=7)



    def __str__(self):
        return self.title
        


class Comment(models.Model):
    pass