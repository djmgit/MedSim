from constants import *

"""
meng ic calculator

"""
def meng_ic(concept, snomed):

	node_max = NODE_MAX
	leaves_max = LEAVES_MAX
	deep_max = DEEP_MAX

	p1 = float(math.log10(snomed.get_min_depth(concept)) / math.log10(deep_max))

	p2=0
	for hyp in list(concept.descendants_no_double()):
		p2 = p2+float(1.0 / snomed.get_min_depth(hyp))

	p2 = math.log(p2+1)
	p2 = float(p2 / math.log(node_max))
	p2 = 1-p2

	ic = p1 * p2
	return ic
