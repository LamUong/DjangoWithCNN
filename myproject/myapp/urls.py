from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.intro, name='intro'),
    url(r'^myapp/$', views.index, name='index'),
    url(r'^myapp/urlLinkSpecified$', views.urlLinkSpecified, name='urlLinkSpecified'),
    url(r'^myapp/fileAttachment$', views.fileAttachment, name='fileAttachment'),
]