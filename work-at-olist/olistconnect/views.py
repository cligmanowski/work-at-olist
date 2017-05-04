# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse
from django.template import loader

from olistconnect.models import *

from olistconnect.serializers import * 

from django.views.generic import ListView

from rest_framework.views import *

# Create your views here.

def index(request):
	
	return render(request,'base.html')

def listChannels(request):

	channels = Channel.objects.all()
	context = {
		'channels' : channels,
	}
	return render(request,"olistconnect/listChannels.html",context)

def listCategories(request, channel_name):

	channel = Channel.objects.get(name=channel_name)
	channelCategories = channel.category_set.all()
	

	context = {
		'categories' : channelCategories,
		'channel' : channel
	}
	return render(request,"olistconnect/listCategories.html",context)

def showCategory(request, channel_name, category_detail):

	category = Category.objects.get(slug=category_detail)
	channel = channel_name
	idparentCategories = CategoryPath.objects.filter(descendant=category)
	parentCategories = []
	subcategories = []
	for path in idparentCategories:
		parentCategories.append(path.ancestor)
	iddescendantCategories = CategoryPath.objects.filter(ancestor=category)
	for path in iddescendantCategories:
		subcategories.append(path.descendant)
	if (parentCategories[0]==None):
		parentCategories=None
	elif ( (subcategories[0].name==category.name) and (len(subcategories)==1) ):
		subcategories = None
	context = {
		'category': category,
		'subcategories': subcategories,
		'parentCategories': parentCategories,
		'channel': channel
	}
	return render(request,"olistconnect/categoryDetail.html", context)

class ListChannels(APIView):
    """
    View to list all channels in the system.

    """ 

    def get(self, request, format=None):
        """
        get:
        Return a list of all channels.
        """
        channels = Channel.objects.all()
        channelSerialized = channelSerializer(channels,many=True)
        return Response(channelSerialized.data)

class ListCategories(APIView):
    """
    View to list all categories in a Channel.

    """ 

    def get(self, request, channel_name, format=None):
        """
        get:
        Return a list of the Channel Categories.
        """
        channel = get_object_or_404(Channel, name=channel_name)
        categories = Category.objects.filter(categoryChannel=channel)
        categorySerialized = categorySerializer(categories,many=True)
        return Response(categorySerialized.data)

   
class ListParentSubCategories(APIView):

	"""
	View to list the Parent Categories and Subcategories of a Particular Category

	"""

	def get(self, request, channel_name, category_slug, format=None):
		"""
        Return a list of Parents and Sub Categories of a Category
        """
		channel = get_object_or_404(Channel, name=channel_name)
		category = get_object_or_404(Category, slug=category_slug, categoryChannel=channel )
		parentCategories = self.getAncestors(category)
		subCategories = self.getDescendants(category)





		parentSerialized = categorySerializer(parentCategories,many=True)
		subSerialized = categorySerializer(subCategories,many=True)

		content = {
			'parents': parentSerialized.data,
			'subcategories': subSerialized.data,
		}

		return Response(content)

	def getAncestors(self,Category):
		"""
        Return a Parents list of a Category
        """
		ancestors = []
		idAncestors = CategoryPath.objects.filter(descendant=Category).exclude(ancestor=Category)
		for path in idAncestors:
			ancestors.append(path.ancestor)

		return ancestors

	def getDescendants(self,Category):
		"""
        Return a Subcategory list of a Category
        """
		descendants = []
		idDescendants = CategoryPath.objects.filter(ancestor=Category).exclude(descendant=Category)
		for path in idDescendants:
			descendants.append(path.descendant)

		return descendants









