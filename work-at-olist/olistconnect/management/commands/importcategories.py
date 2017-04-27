import sys
import csv

from django.core.management.base import BaseCommand, CommandError
from olistconnect.models import *

# todo :
#	process the Category names  
# 	get the Category Name and pass to a Model or Database

class Command(BaseCommand):
    help = ' Import categories from specified CSV file '
    classDict = {}
    channelObj = None

    def add_arguments(self, parser):
    	parser.add_argument('channelName', type=str, help='The channel\'s name that will be stored')
    	parser.add_argument('csvFile', help='The CSV file that has the categories to be imported')

    def handle(self, *args, **options):
    	channel = options['channelName']
    	csvFileName = options['csvFile']
    	

    	try:
    		channelObj = Channel()
    		channelObj.name = channel
    		channelObj.save()
    		self.readFile(csvFileName)

        except:
        	raise CommandError('File "%s" does not exist' % csvFileName)

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
		categoryTreePath = CategoryPath()
		if (pathLen==1):
			category = categories[0].strip()
			# categoryObj = Category(category)
			# self.classDict[category] = categoryObj
			# descendant = categoryObj
		else:
			category = categories[pathLen-1].strip()
			# categoryObj = Category(category)
			# self.classDict[category]=categoryObj
			# descendant = categoryObj 
			ancestor = self.classDict[categories[pathLen-2].strip()]

		categoryObj = Category()
		categoryObj.name = category
		categoryObj.categoryChannel = self.channelObj
		self.classDict[category]=categoryObj
		descendant = categoryObj 
		categoryTreePath.setAncestor(ancestor)
		categoryTreePath.setDescendant(descendant)
		categoryObj.save()
		# categoryTreePath.save()

		print self.classDict
			
		


	# if __name__ == "__main__":
	# 	argumentsNumber = len(sys.argv)
	# 	if (argumentsNumber == 2):
	# 		param = sys.argv[1]
	# 		readFile( param )
	# 	else: 
	# 		print("You need to provide a csv file as argument!")
