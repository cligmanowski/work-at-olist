from django.conf.urls import url
from olistconnect.views import *
# Uncomment this line to enable admin
# from django.contrib import admin


urlpatterns = [
	# Uncomment this line to enable admin
    # url(r'^admin/', admin.site.urls),
    url(r'^$', index),

]
