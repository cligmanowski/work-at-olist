# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader

from olistconnect.models import *
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

	category = Category.objects.get(name=category_detail)
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

