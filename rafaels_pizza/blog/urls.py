from django.conf.urls import url, include
from . import views



urlpatterns = [
	url(r'^$', include(views.blog)),
	url(r'^category/(?P<c_id>[\-\w]+)/$', include(views.category)),
	url(r'^post/(?P<p_id>[\-\w]+)/$', include(views.post)),
]
