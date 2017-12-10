from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       url(r'^$', 'books.views.home', name='home'),
                       url(r'^books/', 'books.views.view_all_books', name='view_all_books')
                       )
