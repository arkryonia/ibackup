from django.conf.urls import url
from django.core.urlresolvers import reverse

from foton.theme import  views

urlpatterns = [

	url(
		regex = r'^$',
		view = views.Allianza.as_view(),
		name='allianza'
	),

]