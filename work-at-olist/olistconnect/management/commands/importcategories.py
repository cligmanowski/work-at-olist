import sys
import csv

from django.core.management.base import BaseCommand, CommandError

# todo :
#	process the Category names  
# 	get the Category Name and pass to a Model or Database

class Command(BaseCommand):
    help = ' Import categories from specified CSV file '

    def add_arguments(self, parser):
    	parser.add_argument('csvFile')

    def handle(self, *args, **options):
    	csvFileName = options['csvFile']
    	try:
    		self.readFile(csvFileName)

        except:
        	raise CommandError('File "%s" does not exist' % csvFileName)

        self.stdout.write(self.style.SUCCESS('CSV file "%s" Successfully read' % csvFileName))

    def readFile(self, csvFileName):
    	with open(csvFileName) as csvFile:

			read = csv.DictReader(csvFile)

			for row in read:
				categoryPath = row['Category'];
				if (categoryPath!=""):
					for categories in categoryPath.split("/"):
						print(categories)


	

	# if __name__ == "__main__":
	# 	argumentsNumber = len(sys.argv)
	# 	if (argumentsNumber == 2):
	# 		param = sys.argv[1]
	# 		readFile( param )
	# 	else: 
	# 		print("You need to provide a csv file as argument!")
