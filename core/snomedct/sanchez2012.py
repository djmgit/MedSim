from constants import *
import math

"""
sanchez2012 ic calculator

"""
def sanchez2012_snomed(concept, snomed):

	node_max=NODE_MAX
	leaves_max=LEAVES_MAX
	deep_max=DEEP_MAX

	ic=float(commonness(concept)/19664.6949438)
	
	ic=-1*math.log10(ic)
	return ic


def commonness(concept):
	if len(concept.children)==0:
		subsumer_no=len(list(concept.ancestors_no_double()))+1
		return float(1.0/subsumer_no)
	leaves=snomed.get_all_leaves()
	s=0
	for leaf in snomed.get_concept_leaves(concept):
		subsumer_no=len(list(leaf.ancestors_no_double()))+1		
		s=s+float(1.0/subsumer_no)
	return s
