from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager
from django.contrib.auth.models import User

# Create your models here.

'''
   - fields , options
   - validation
   - html widget

'''

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=30000)
    create_date = models.DateTimeField(default='')
    draft = models.BooleanField(default=True)
    tags = TaggableManager()
    image = models.ImageField('img/')
    auther = models.ForeignKey(User , on_delete=models.SET_NULL, null=True)




    def __str__(self) -> str:
        return self.title
        


class Comment(models.Model):
    pass