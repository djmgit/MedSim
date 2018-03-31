from constants import *

"""
sanchez2011 ic calculator

"""
def sanchez2011_snomed(concept):
	
	node_max=NODE_MAX
	leaves_max=LEAVES_MAX
	deep_max=DEEP_MAX

	leaves_no=snomed.get_num_concept_leaves(concept)
	subsumer_no=len(list(concept.ancestors_no_double()))+1

	p1=float(leaves_no/subsumer_no)+1.0
	p1=float(p1/(leaves_max+1))
	ic=(-1.0)*math.log10(p1)
	return ic
