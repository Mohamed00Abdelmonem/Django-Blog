from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
# from django_summernote.fields import SummernoteTextFormField, SummernoteTextField
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
    create_date = models.DateTimeField(default=timezone.now)
    draft = models.BooleanField(default=True)
    tags = TaggableManager()
    image = models.ImageField(upload_to='posts')
    auther = models.ForeignKey(User , on_delete=models.SET_NULL, null=True)
    

    def __str__(self):
        return self.title
        


class Comment(models.Model):
    author = models.ForeignKey(User, related_name='comment_author', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment_post')
    comment = models.TextField(max_length=500)
    create_at = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return f'created comment by {self.author} on post {self.post}'




