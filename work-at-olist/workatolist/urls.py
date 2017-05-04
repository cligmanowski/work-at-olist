from django.conf.urls import url, include
from olistconnect.views import *
# Uncomment this line to enable admin
# from django.contrib import admin

from rest_framework.documentation import include_docs_urls


#router = routers.DefaultRouter()

#router.register(r'^' , ChannelView),


urlpatterns = [
	# Uncomment this line to enable admin
    # url(r'^admin/', admin.site.urls),
    # url(r'^$', index),
    url(r'^$', ListChannels.as_view(), name='channellist'),
    url(r'^docs/', include_docs_urls(title='OList Assingment')),
    url(r'^channels/(?P<channel_name>\w+)$', ListCategories.as_view(),name='listcategories'),
    url(r'^channels/(?P<channel_name>\w+)/(?P<category_slug>[\w-]+)$', ListParentSubCategories.as_view(),name='categorydetail'),
   
    
    # url(r'^channelsHtml$', listChannels, name='channels'),
    # url(r'^channelsHtml/(?P<channel_name>\w+)$', listCategories, name='list_categories'),
    # url(r'^channelsHtml/(?P<channel_name>\w+)/(?P<category_detail>[\w-]+)$', showCategory, name='category_detail')
]
