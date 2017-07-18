"""django_reddit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
import debug_toolbar
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter

from web import views
from web.api import views as api_views

router = DefaultRouter()
router.register(r'reddits', api_views.RedditViewSet)
router.register(r'articles', api_views.ArticleViewSet)

urlpatterns = [
    url(r'^__debug__/', include(debug_toolbar.urls)),
    url(r'^api/', include(router.urls, namespace='api')),
    url(r'^admin/', admin.site.urls),
    url(r'^r/(?P<slug>[a-zA-Z0-9\-]+)/$', views.RedditDetail.as_view(), name='reddit-detail'),
    url(r'', views.home, name='home')
]
