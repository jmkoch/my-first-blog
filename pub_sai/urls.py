from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from pub import views

urlpatterns = [
    url(r'^browse/$',views.browse_pubs, name="pub_browse_base"),
    url(r'^browse/query$',views.browse_query_pubs, name="pub_browse_query"),
    url(r'^browse/([a-zA-Z0-9_-]+)/$',views.browse_single, name="pub_browse_single"),
    url(r'^browse/([a-zA-Z0-9_-]+)/update$',views.pub_update, name="pub_update"),
    url(r'^browse/([a-zA-Z0-9_-]+)/delete$',views.pub_delete, name="pub_delete"),
    url(r'^bfile/$', views.upload_bfile, name="pub_browse_upload_bfile"),
    url(r'^single/$',views.enter_single_publication, name="pub_browse_upload_single")
]