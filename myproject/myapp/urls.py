from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^urlLinkSpecified$', views.urlLinkSpecified, name='urlLinkSpecified'),
    url(r'^fileAttachment$', views.fileAttachment, name='fileAttachment'),
]