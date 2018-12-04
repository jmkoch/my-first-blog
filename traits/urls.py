from django.conf.urls import url
from traits.views import TraitCreateView#, AddressCreateView
#from traits.forms import AddressForm

urlpatterns = [
	url(r'^trait/create/$', TraitCreateView.as_view(), name="create trait"),
	#url(r'^address/create/$', AddressCreateView.as_view(), name="address form"),
]