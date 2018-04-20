"""
This is the core class that excepts a ontology,
a ic model, a similarity model, and returns
correlation

"""

from benchmarks import benchmark
from snomedct import *
from mesh import *
from similarity_models import *
from SnomeCrawl import *
import pickle
import math
from corr import get_corr
from MeshCrawl import *
import math
import os

snomed=Scrawl()
mcrawl=Mcrawl()

from utils import *

class MedCore:
	def __init__(self):
		self.bm_snomed = benchmark['SNOMEDCT']
		self.bm_mesh = benchmark['MESH']
		self.BASE_DIR = os.path.dirname(os.path.abspath(__file__))

		self.load_ic_models()
		self.load_similarity_models()

	def init_core(self, ontology, ic_model, similarity_model):
		self.ontology = ontology
		self.ic_model = ic_model
		self.similarity_model = similarity_model

		self.load_data()
		self.calculate_ic()
		self.calculate_sim()
		self.calculate_corr()

	def load_data(self):
		if self.ontology == 'SNOMEDCT':
			self.data = self.load_data_util(os.path.join(self.BASE_DIR, 'data/data_snomed.txt'))
		else:
			self.data = self.load_data_util(os.path.join(self.BASE_DIR, 'data/data_mesh.txt'))

	def load_data_util(self, file_name):
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
		self.ic_models_snomed['zhou'] = zhou_snomed
		self.ic_models_snomed['seco'] = seco_snomed


		# setup ic models for mesh
		self.ic_models_mesh['hadj'] = hadj_mesh
		self.ic_models_mesh['harispe'] = harispe_mesh
		self.ic_models_mesh['meng'] = meng_mesh
		self.ic_models_mesh['our'] = our_mesh
		self.ic_models_snomed['quingbo'] = quingbo_mesh
		self.ic_models_mesh['sanchez2011'] = sanchez2011_mesh
		self.ic_models_mesh['sanchez2012'] = sanchez2012_mesh
		self.ic_models_mesh['zhou'] = zhou_mesh
		self.ic_models_mesh['seco'] = seco_mesh

	def load_similarity_models(self):
		self.similarity_models = {}

		# setup similairty models
		self.similarity_models['resnik'] = resnik
		self.similarity_models['lin'] = lin
		self.similarity_models['jian'] = jian
		self.similarity_models['pirro'] = pirro
		self.similarity_models['batet'] = batet
		self.similarity_models['menggu'] = menggu
		self.similarity_models['our'] = our

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
		print 'Calculating IC values...\n'

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
				ic_mica = get_lca_snomed(concept1, concept2, util_library, self.ic_selected)
			else:
				concept1, concept2 = mesh[concept1], mesh[concept2]
				ic_mica = get_lca_mesh(concept1, concept2, util_library, self.ic_selected)

			ic_concept1 = self.ic_selected(concept1, util_library)
			ic_concept2 = self.ic_selected(concept2, util_library)

			IC_CONCEPTS[concept1_str] = ic_concept1
			IC_CONCEPTS[concept2_str] = ic_concept2
			IC_CONCEPTS['{}&{}'.format(concept1_str, concept2_str)] = ic_mica

			print '{} : {}'.format(concept1_str, str(ic_concept1))
			print '{} : {}'.format(concept2_str, str(ic_concept2))
			print 'LCS {} {} : {}'.format(concept1_str, concept2_str, str(ic_mica))
			print '\n'

		print 'IC values computation done\n'

		self.ic_concepts = IC_CONCEPTS

	def calculate_sim(self):
		
		# select similarity model
		print 'Calculating similarity values...\n'

		self.sim_selected = self.similarity_models[self.similarity_model]

		# list to store similarities
		self.sim_val = []

		for concepts in self.data:
			term1 = concepts[0]
			term2 = concepts[1]

			concept1, concept2 = '', ''
			util_library = ''
			graph = ''
			if self.ontology == 'SNOMEDCT':
				concept1, concept2 = SNOMEDCT[int(term1)], SNOMEDCT[int(term2)]
				util_library = snomed
				graph = SNOMEDCT
			else:
				concept1, concept2 = mesh[term1], mesh[term2]
				util_library = mcrawl
				graph = mesh

			sim = self.sim_selected(term1, term2, concept1, concept2, self.ic_concepts, self.ontology, self.ic_selected, util_library, graph)
			self.sim_val.append(sim)

		print 'Similarity values computation done\n'

	def calculate_corr(self):
		print 'Calculating correlations...\n'
		if self.ontology == 'SNOMEDCT':
			self.corr_physical = get_corr(self.sim_val, self.bm_snomed['ben'])
			self.corr_medical = get_corr(self.sim_val, self.bm_snomed['ben2'])
			self.corr_average = get_corr(self.sim_val, self.bm_snomed['ben3'])
		else:
			self.corr_physical = get_corr(self.sim_val, self.bm_mesh['ben'])
			self.corr_medical = get_corr(self.sim_val, self.bm_mesh['ben2'])
			self.corr_average = get_corr(self.sim_val, self.bm_mesh['ben3'])

		print 'Correlation computation done\n'

	def get_corr(self):
		return self.corr_physical, self.corr_medical, self.corr_average

	def get_sim_val(self):
		return self.sim_val

	def get_ic_val(self):
		return self.ic_concepts

	def get_data(self):
		return self.data
