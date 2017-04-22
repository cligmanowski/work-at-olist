import sys
import csv

from django.core.management.base import BaseCommand, CommandError

# todo :
#	process the Category names  
# 	get the Category Name and pass to a Model or Database

class Command(BaseCommand):
    help = ' Import categories from specified CSV file '

    def add_arguments(self, parser):
    	
        parser.add_argument('csvFile', type=file)

    def handle(self, *args, **options):
        print("ola")
        try:
            readFile(csvFile)

        except fileProblem:
            raise CommandError('File "%s" does not exist' % csvFile)

        self.stdout.write(self.style.SUCCESS('CSV file "%s" Successfully read' % csvFile))

	def readFile( csvFileName ):

		with open(csvFileName) as csvFile:
			read = csv.DictReader(csvFile)

			for row in read:

				print(row['Category']);

	# if __name__ == "__main__":
	# 	argumentsNumber = len(sys.argv)
	# 	if (argumentsNumber == 2):
	# 		param = sys.argv[1]
	# 		readFile( param )
	# 	else: 
	# 		print("You need to provide a csv file as argument!")
