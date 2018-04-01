from constants import *

"""
sanchez2012 ic calculator

"""
def sanchez2012_mesh(concept, mcrawl):

	
	node_max=NODE_MAX
	leaves_max=LEAVES_MAX
	deep_max=DEEP_MAX

	ic=float(commonness(concept)/27781.0331121)
	
	ic=-1*math.log10(ic)
	return ic


def commonness(concept):
	if len(concept.children)==0:
		subsumer_no=len(list(set(concept.rparents())))+1
		return float(1.0/subsumer_no)
	s=0
	for leaf in mcrawl.get_concept_leaves(concept):
		subsumer_no=len(list(set(leaf.rparents())))+1		
		s=s+float(1.0/subsumer_no)
	return s