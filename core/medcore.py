"""
This is the core class that excepts a ontology,
a ic model, a similarity model, and returns
correlation

"""

from benchmarks import *
from snomedct import *
from mesh import *
from pymedtermino import *
from pymedtermino.snomedct import *
from SnomeCrawl import *
import pickle
import math
from utils import *

from MeshCrawl import *
import math

snomed=Scrawl()
mcrawl=Mcrawl()

class MedCore:
	def __init__(self, ontology, ic_model, similarity_model):
		self.ontology = ontology
		self.ic_model = ic_model
		self.similarity_model = similarity_model
		self.bm_physical = ben
		self.bm_medical = ben2
		self.bm_average = ben3

		self.load_data()
		self.load_ic_models()

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

	def load_ic_models(self):
		self.ic_models_snomed = {}
		self.ic_models_mesh = {}
		
		# setup ic models for snomect
		self.ic_models_snomed['hadj'] = hadj_snomed
		self.ic_models_snomed['harispe'] = harispe_snomed
		self.ic_models_snomed['meng'] = meng_snomed
		self.ic_models_snomed['our'] = our_snomed
		self.ic_models_snomed['quingbo'] = quingbo_snomed
		self.ic_models_snomed['sanchez2011'] = sanchez2011_snomed
		self.ic_models_snomed['sanchez2012'] = sanchez2012_snomed

		# setup ic models for mesh
		self.ic_models_mesh['hadj'] = hadj_mesh
		self.ic_models_mesh['harispe'] = harispe_mesh
		self.ic_models_mesh['meng'] = meng_mesh
		self.ic_models_mesh['our'] = our_mesh
		self.ic_models_snomed['quingbo'] = quingbo_mesh
		self.ic_models_mesh['sanchez2011'] = sanchez2011_mesh
		self.ic_models_mesh['sanchez2012'] = sanchez2012_mesh

	def calculate_ic(self):

		# dictionary to store ic values
		IC_CONCEPTS = {}

		# select util library
		util_library = ''

		# select a ic model
		if self.ontology == 'SNOMEDCT':
			self.ic_selected = self.ic_models_snomed[self.ic_model]
			util_library = snomed
		else:
			self.ic_selected = self.ic_models_mesh[self.ic_model]
			util_library = mcrawl

		# calculate ic values
		for concepts in self.data:
			concept1_str = concepts[0]
			concept2_str = concepts[1]

			concept1 = ''
			concept2 = ''
			ic_concept1 = ''
			ic_concept2 = ''
			ic_mica = ''

			if self.ontology == 'SNOMEDCT':
				concept1, concept2 = SNOMEDCT[int(concept1_str)], SNOMEDCT[int(concept2_str)]
				ic_mica = get_lca_snomed(concept1, concept2, util_library)
			else:
				concept1, concept2 = mesh[concept1], mesh[concept2]
				ic_mica = get_lca_mesh(concept1, concept2, util_library)

			ic_concept1 = self.ic_selected(concept1, util_library)
			ic_concept2 = self.ic_selected(concept2, util_library)

			IC_CONCEPTS[concept1_str] = ic_concept1
			IC_CONCEPTS[concept2_str] = ic_conecpt2
			IC_CONCEPTS['{}&{}'.format(concept1_str, concept2_str)] = ic_mica

		self.ic_concepts = IC_CONCEPTS
