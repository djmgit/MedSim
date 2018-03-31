from constants import *

"""
harispe ic calculator

"""
from constants import *

"""
harispe ic calculator

"""
def harispe_snomed(concept, snomed):

	node_max=NODE_MAX
	leaves_max=LEAVES_MAX
	deep_max=DEEP_MAX

	no_of_leaves = snomed.get_num_concept_leaves(concept) + 1
	subsumer_no = len(list(concept.ancestors_no_double())) + 1

	num = float(no_of_leaves)/ float(subsumer_no)
	den = leaves_max
	ic = math.log10(float(num/den))
	ic = -1 * ic
	return ic
