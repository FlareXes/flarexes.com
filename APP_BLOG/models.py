from django.db import models
from taggit.managers import TaggableManager

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    thumbnail = models.ImageField(blank=True, null=True)
    content = models.TextField()                                # this has to be `content` variable
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    tags = TaggableManager(blank=True)

    def __str__(self):
        return self.title
