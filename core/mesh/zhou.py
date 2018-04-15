from constants import *
import math

"""
zhou ic calculator

"""
def zhou_mesh(concept, mcrawl):
	node_max=NODE_MAX
	leaves_max=LEAVES_MAX
	deep_max=DEEP_MAX

	hypo=len(list(set(concept.rchildren())))+1
	p1=float(math.log10(hypo)/math.log10(node_max))
	p1=1-p1

	p2=float(math.log10(mcrawl.get_min_depth(concept))/math.log10(deep_max))

	k=float(0.5)
	ic=(k*p1)+((1-k)*p2)
	return ic
	