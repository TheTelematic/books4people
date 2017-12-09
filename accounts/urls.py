from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       url(r'^$', 'accounts.views.login', name='login'),
                       )
