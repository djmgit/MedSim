from constants import *

"""
seco ic calculator

"""
def seco_mesh(concept, mcrawl):
	
	node_max=NODE_MAX
	leaves_max=LEAVES_MAX
	deep_max=DEEP_MAX

	hypo=len(list(set(concept.rchildren())))
	p1=math.log10(float((hypo+1.0)/node_max))

	p2=math.log10(float(1.0/node_max))

	ic=float(p1/p2)
	return ic	
