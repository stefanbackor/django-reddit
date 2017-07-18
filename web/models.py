from django.db import models

# Create your models here.

class Reddit(models.Model):
    name = models.CharField(max_length=255, blank=False)
    slug = models.SlugField(max_length=255, unique=True, blank=False)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return  '%s - %s' % (self.pk, self.name)

class Article(models.Model):
    url = models.URLField()
    description = models.TextField(blank=True)
    reddit = models.ForeignKey(Reddit)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

class Comment(models.Model):
    text = models.TextField()
    article = models.ForeignKey(Article)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
