from constants import *

"""
zhou ic calculator

"""
def zhou_snomed(concept, snomed):
	node_max = NODE_MAX
	leaves_max = LEAVES_MAX
	deep_max = DEEP_MAX

	hypo = len(list(concept.descendants_no_double())) + 1
	p1 = float(math.log10(hypo)/math.log10(node_max))
	p1 = 1 - p1

	p2 = float(math.log10(snomed.get_min_depth(concept)) / math.log10(deep_max))

	k = float(0.5)
	ic = (k*p1)+((1-k)*p2)

	return ic
