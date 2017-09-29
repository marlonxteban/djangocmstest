from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

from django.conf.urls import url
from .views import *


class BlogApp(CMSApp):
	"""docstring for BlogApp"""
	app_name = 'blog'
	name = _('Blog')
	urls = ['blog.urls', ]
	
apphook_pool.register(BlogApp)