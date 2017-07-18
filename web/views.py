from django.shortcuts import render, render_to_response
from django.views.generic import DetailView
from . import models
# Create your views here.

def home(request):
    return render(request, 'web/home.html', { 'reddits': models.Reddit.objects.all() })


class RedditDetail(DetailView):
    model = models.Reddit
