"""
This is the core class that excepts a ontology,
a ic model, a similarity model, and returns
correlation

"""

class MedCore:
	def __init__(self, ontology, ic_model, similarity_model):
		self.ontology = ontology
		self.ic_model = ic_model
		self.similarity_model = similarity_model

		self.load_data()
		self.load_benchmark()

	def load_data(self):
		if self.ontology == 'SNOMED':
			self.data = load_data_util('data/data_snomed.txt')
		else:
			self.data = load_data_util('data/data_mesh.txt')

	def load_data_util(file_name):
		data_file = open(file_name)
		data_file_lines = data_file.readlines()
	
		data = []
		for line in data_file_lines:
			concepts = line.split()
			data.append((concepts[0], concepts[1]))
	
		return data

	