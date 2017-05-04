from olistconnect.models import *
from rest_framework import serializers

class channelSerializer(serializers.ModelSerializer):
	# Serialize all the channels 

	class Meta:
		model = Channel
		fields = ('id','name')

class categorySerializer(serializers.ModelSerializer):
	categoryChannel = channelSerializer(read_only=True)
	class Meta:
		model = Category
		fields = ( 'id','name','slug','categoryChannel')

class pathSerializer(serializers.ModelSerializer):
	ancestor = categorySerializer(read_only=True)
	descendant = categorySerializer(read_only=True)

	class Meta:
		model = CategoryPath
		fiels = ('id','ancestor','descendant')

