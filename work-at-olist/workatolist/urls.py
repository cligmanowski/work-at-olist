from django.conf.urls import url, include
from olistconnect.views import *
# Uncomment this line to enable admin
# from django.contrib import admin
from rest_framework import routers

#router = routers.DefaultRouter()

#router.register(r'^' , ChannelView),


urlpatterns = [
	# Uncomment this line to enable admin
    # url(r'^admin/', admin.site.urls),
    url(r'^$', ListChannels.as_view()),
    url(r'^channels/(?P<channel_name>\w+)$', ListCategories.as_view()),
    url(r'^channels/(?P<channel_name>\w+)/(?P<category_slug>[\w-]+)$', ListParentSubCategories.as_view())
    # url(r'^$', views.ChannelView, name="channel_list"),
    # url(r'^channels$', listChannels, name='channels'),
    # url(r'^channels/(?P<channel_name>\w+)$', listCategories, name='list_categories'),
    # url(r'^channels/(?P<channel_name>\w+)/(?P<category_detail>[\w-]+)$', showCategory, name='category_detail')
]
