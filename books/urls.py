from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       url(r'^$', 'books.views.home', name='home'),
                       )