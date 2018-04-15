from constants import *
import math

"""
quingbo ic calculator

"""
def quingbo_snomed(concept, snomed):

	node_max=NODE_MAX
	leaves_max=LEAVES_MAX
	deep_max=DEEP_MAX

	f_depth = float(math.log10(snomed.get_min_depth(concept))/math.log10(deep_max))
	f_leaves = float(math.log10(snomed.get_num_concept_leaves(concept)+1)/math.log10(leaves_max+1))
	f_hyp = float(math.log10(len(list(concept.ancestors_no_double()))+2)/math.log10(node_max))

	return f_depth*(1-f_leaves)+f_hyp
