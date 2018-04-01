"""
This is the core class that excepts a ontology,
a ic model, a similarity model, and returns
correlation

"""

from benchmarks import *

class MedCore:
	def __init__(self, ontology, ic_model, similarity_model):
		self.ontology = ontology
		self.ic_model = ic_model
		self.similarity_model = similarity_model
		self.bm_physical = ben
		self.bm_medical = ben2
		self.bm_average = ben3

		self.load_data()

	def load_data(self):
		if self.ontology == 'SNOMED':
			self.data = load_data_util('data/data_snomed.txt')
		else:
			self.data = load_data_util('data/data_mesh.txt')

	def load_data_util(self, ile_name):
		data_file = open(file_name)
		data_file_lines = data_file.readlines()
	
		data = []
		for line in data_file_lines:
			concepts = line.split()
			data.append((concepts[0], concepts[1]))
	
		return data

	def calculate_ic(self):
		pass


