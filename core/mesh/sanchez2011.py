from constants import *
import math

"""
sanchez2011 ic calculator

"""
def sanchez2011_mesh(concept, mcrawl):
	
	node_max=NODE_MAX
	leaves_max=LEAVES_MAX
	deep_max=DEEP_MAX

	leaves_no=mcrawl.get_num_concept_leaves(concept)
	subsumer_no=len(list(set(concept.rparents())))+2.0

	p1=float(leaves_no/subsumer_no)+1.0
	#print p1
	p1=float(p1/(leaves_max+1))
	ic=(-1.0)*math.log10(p1)
	return ic
