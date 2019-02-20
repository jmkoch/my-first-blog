from django.conf.urls import url
from pubs.views import PubCreateView, export_pubs_csv

urlpatterns = [
    url(r'^pub/create/$', PubCreateView.as_view(success_url = 'successful_upload.html'), name="create pub"),
    url(r'^export/pubs/csv/$', export_pubs_csv, name='export_pubs_csv'),

]