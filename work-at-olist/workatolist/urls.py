from django.conf.urls import url
from olistconnect.views import *
# Uncomment this line to enable admin
# from django.contrib import admin


urlpatterns = [
	# Uncomment this line to enable admin
    # url(r'^admin/', admin.site.urls),
    url(r'^$', index),
    url(r'^channels$', listChannels, name='channels'),
    url(r'^channels/(?P<channel_name>\w+)$', listCategories, name='list_categories'),
    url(r'^channels/(?P<channel_name>\w+)/(?P<category_detail>[\w-]+)$', showCategory, name='category_detail')
]
