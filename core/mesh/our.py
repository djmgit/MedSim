from constants import *
import math


"""
our ic calculator

"""
def our_mesh(concept, mcrawl):

	
	node_max=NODE_MAX
	leaves_max=LEAVES_MAX
	deep_max=DEEP_MAX

	p1=float(math.log10(mcrawl.get_min_depth(concept)+1.0)/math.log10(deep_max+1.0))

	nmih_no=len(list(set(concept.parents)))
	leaves_no=mcrawl.get_num_concept_leaves(concept)

	subsumer_no=len(list(set(concept.rparents())))+2.0

	p2=(1-math.log10(float(float((leaves_no*nmih_no)/leaves_max)/subsumer_no)+1.0))

	hypo=list(set(concept.rchildren()))

	s=0
	for h in hypo:
		
		s=s+float(1.0/mcrawl.get_min_depth(h))
	s+=1.0
	p3=(1-float(math.log10(s)/math.log10(node_max)))

	ic=p1*p2*p3
	return ic
