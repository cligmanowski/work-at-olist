# -*- coding: utf-8 -*-
import sys
import csv

from django.core.management.base import BaseCommand, CommandError
from django.db.utils import IntegrityError
from olistconnect.models import *

class Command(BaseCommand):
    help = ' Import categories from specified CSV file '
    
    channelObj = None
    

    def add_arguments(self, parser):
    	parser.add_argument('channelName', type=str, help='The channel\'s name that will be stored')
    	parser.add_argument('csvFile', help='The CSV file that has the categories to be imported')

    def handle(self, *args, **options):
    	channel = options['channelName']
    	csvFileName = options['csvFile']
    	

    	try:
    		self.channelObj = Channel()
    		self.channelObj.name = channel
    		self.channelObj.save()
    		self.readFile(csvFileName)

        except CommandError,IntegrityError:
        	raise CommandError('File "%s" does not exist' % csvFileName)
        	raise IntegrityError('Already has a channel named "%s"' % channel)

        self.stdout.write(self.style.SUCCESS('CSV file "%s" Successfully read' % csvFileName))

    def readFile(self, csvFileName):
    	with open(csvFileName) as csvFile:

			read = csv.DictReader(csvFile) 

			for row in read:
				categoryPath = row['Category']
				if (categoryPath!=""):
					self.saveCategories(categoryPath)

    def saveCategories(self,categoryPath):
		categories = categoryPath.split("/")
		pathLen = len(categories)
		ancestor = None
		descendant = None
		categoryObjList = []
		categoryObj = None
		categoryTreeObj = None
		if (pathLen==1):
			category = categories[0].strip()
			categoryObj = Category()
			categoryTreeObj = CategoryPath()
			categoryObj.name = category
			categoryObj.categoryChannel = self.channelObj
			categoryObj.save()
			categoryTreeObj.setDescendant(categoryObj)
			categoryTreeObj.setAncestor(ancestor)
			categoryTreeObj.save()
		else:
			for count in range(0,pathLen-1):
				category = categories[count].strip()
				# print('Buscando "%s" no banco de dados' % category)
				categoryObj = Category.objects.get(name=category)
				# if categoryObj:
				# 	print('Categoria "%s" encontrada com sucesso' % categoryObj.name)
				categoryObjList.append(categoryObj)
			categoryObj = Category()
			categoryObj.name = categories[pathLen-1].strip()
			categoryObj.categoryChannel = self.channelObj
			categoryObj.save()
			categoryObjList.append(categoryObj)
			descendant = categoryObj
			objLen = len(categoryObjList)
			for ancestor in categoryObjList:
				print ancestor.name
				categoryTreeObj = CategoryPath()
				categoryTreeObj.setAncestor(ancestor)
				categoryTreeObj.setDescendant(descendant)
				categoryTreeObj.save()

			

		