from django.conf.urls import patterns, include, url
from django.contrib import admin
from blog.views import all_articles, article_read

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'my_blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',all_articles),  
    url(r'^(?P<article_id>)/$',article_read),  
)
