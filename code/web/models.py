from django.db import models


class Reddit(models.Model):
    name = models.CharField(max_length=255, blank=False)
    slug = models.SlugField(max_length=255, unique=True, blank=False)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return '%s - %s' % (self.pk, self.name)


class Article(models.Model):
    url = models.URLField()
    description = models.TextField(blank=True)
    reddit = models.ForeignKey(Reddit, related_name='articles')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.url


class Comment(models.Model):
    text = models.TextField()
    article = models.ForeignKey(Article)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
