"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from home import views
from django.contrib.auth import views as authviews

urlpatterns = [
    # attr name for url title name
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='home'),
    url(r'^blog/$', views.blog, name='blog'),
    url(r'^writing/$', views.writing, name='writing'),
    url(r'^writing/(?P<pk>[0-9]+)/modification/$', views.modification, name='modification'),
    url(r'^detail/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    url(r'^drafts/$', views.draft_list, name='drafts'),
    url(r'^post/(?P<pk>[0-9]+)/publish/$', views.post_publish, name='post_publish'),
    url(r'^writing/(?P<pk>[0-9]+)/remove/$', views.remove, name='remove'),
    url(r'^archives/$', views.archives, name='archives'),
    url(r'^search_tag/(?P<tag>\w+)/$', views.search_tag, name='search_tag'),
    url(r'^aboutme/$', views.about_me, name='about_me'),
    url(r'^accounts/login/$', authviews.login, {'template_name': 'blog/login.html'}, name='login'),
    url(r'^accounts/logout/$', authviews.logout, name='logout', kwargs={'next_page': '/'}),
    url(r'^search/$', views.blog_search, name='search'),
    url(r'^work/$', views.work, name='work'),
]
