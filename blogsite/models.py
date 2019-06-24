import uuid
from datetime import date
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

# Create your models here.

class Blogger(models.Model):

    username = models.CharField(max_length=32, primary_key=True)
    bio = models.CharField(max_length=144, help_text="Enter a short biography.")
    # id = models.UUIDField(default=uuid.uuid4, help_text="Unique ID for blogger")

    def __str__(self):
        return f'{self.username}'

    def get_absolute_url(self):
        return reverse('blogger-detail', args=[str(self.pk)])


class BlogPost(models.Model):

    name = models.CharField(max_length=122, help_text="Enter name for blog post.")
    content = models.TextField(help_text="Enter content of blog post.")
    author = models.ForeignKey('Blogger', on_delete=models.SET_NULL, null=True)
    post_date = models.DateField(default=date.today)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blogpost-detail', args=[str(self.id)])

    class Meta:
        ordering = ['-post_date']
        # permissions = (
        #     ('is_blogger', 'User can write blog posts.'),
        # )




class Comment(models.Model):

    post = models.ForeignKey('BlogPost', on_delete=models.SET_NULL, null=True)
    date = models.DateField(auto_now_add=True)
    content = models.CharField(max_length=256, help_text="Enter comment.")
    commenter = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.content)

    class Meta:
        ordering = ['date']
        permissions = (
            ('can_comment', 'User can comment on posts'),
        )