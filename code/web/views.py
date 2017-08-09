from django.shortcuts import render, render_to_response
from django.views.generic import DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from . import models


def home(request):
    return render(request, 'web/home.html', {
        'reddits': models.Reddit.objects.all()})


class WebViewMixin(object): # LoginRequiredMixin
    model = models.Reddit

class RedditDetail(WebViewMixin, DetailView):
    pass

class RedditAdd(WebViewMixin, CreateView):
    pass
