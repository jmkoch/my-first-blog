from django.conf.urls import url
from traits.views import TraitCreateView

urlpatterns = [
	url(r'^trait/create/$', TraitCreateView.as_view(), name="create trait"),
]