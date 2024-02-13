from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
class Post(models.Model):
    class Statues(models.TextChoices):
        DRAFT='DF','Draft'
        PUPILISHED='PB','Pupilished'

    title=models.CharField(max_length=100)
    slug=models.SlugField(max_length=100)
    body=models.TextField()
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_posts')
    puplish=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    statues=models.CharField(max_length=2,choices=Statues.choices,default=Statues.DRAFT)
    def __str__(self):
        return self.title
    class Meta:
        ordering=('-puplish',)
        indexes=[models.Index(fields=['-puplish']),
        ]
