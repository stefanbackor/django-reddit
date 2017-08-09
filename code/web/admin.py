from django.contrib import admin

from . import models


class RedditAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


# Register your models here.
admin.site.register(models.Reddit, RedditAdmin)
admin.site.register(models.Article)
admin.site.register(models.Comment)
