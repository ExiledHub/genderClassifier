import csv
 
class Dataset(object):
	def __init__(self):
		self.names     = []
		self.genders   = []
		self.loadData()
		

	def loadData(self):
		self.names   = []
		self.genders = []
		csvReader    = csv.reader(open('dataset/dataset.csv'))
		for row in csvReader:
			self.names.append(row[0])
			self.genders.append(0 if row[1] is 'f' else 1)