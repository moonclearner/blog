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
from django.conf.urls import include
from django.contrib import admin
from home import views
from django.contrib.auth import views as authviews
from django.contrib.staticfiles.urls import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#  import debug_toolbar

urlpatterns = [
    # attr name for url title name
    url(r'^admin/', admin.site.urls),
    url(r'^aboutme/$', views.about_me, name='about_me'),
    url(r'^accounts/login/$', authviews.login, {'template_name': 'blog/login.html'}, name='login'),
    url(r'^accounts/logout/$', authviews.logout, name='logout', kwargs={'next_page': '/'}),
    url(r'^$', views.index, name='home'),
    url(r'^blog/$', views.blog, name='blog'),
    url(r'^blog/detail/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    url(r'^writing/$', views.writing, name='writing'),
    url(r'^writing/(?P<pk>[0-9]+)/modification/$', views.modification, name='modification'),
    url(r'^writing/drafts/$', views.draft_list, name='drafts'),
    url(r'^writing/(?P<pk>[0-9]+)/publish/$', views.publish, name='publish'),
    url(r'^writing/(?P<pk>[0-9]+)/remove/$', views.remove, name='remove'),
    url(r'^condition/(?P<condition>\w+)/(?P<mode>\w+)/$', views.search_condition, name='search_condition'),
    url(r'uploadtomarkdown/$', views.uploadfiletomarkdown, name='uploadmarkdown'),
    url(r'^search/(?P<searchcontent>\w+)/$', views.blog_search, name='search'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
# django_debug
#  if settings.DEBUG:
#      urlpatterns += [
#          url(r'^__debug__/', include(debug_toolbar.urls)),
#      ]
