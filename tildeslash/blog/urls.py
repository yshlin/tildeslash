from django.conf.urls.defaults import *

from . import views


urlpatterns = patterns('',
    url(r'^$', views.home, name='blog.home'),
    url(r'^posts/(?P<slug>([-_A-z0-9]+))/$', views.post, name='blog.post'),
    url(r'^page/$', views.paged_posts, name='paged.posts'),
    url(r'^page/(?P<page>([0-9]+))/$', views.paged_posts, name='paged.posts'),
    url(r'^tags/(?P<slug>([-_A-z0-9]+))/$', views.tagged_posts, name='tagged.posts'),
    url(r'^tags/(?P<slug>([-_A-z0-9]+))/(?P<page>([0-9]+))/$', views.tagged_posts, name='tagged.posts'),
    url(r'^browserid/', include('django_browserid.urls')),
    url(r'^logout/?$', 'django.contrib.auth.views.logout', {'next_page': '/'},
        name='examples.logout'),
)
