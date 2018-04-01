from constants import *

"""
harispe ic calculator

"""
def harispe_mesh(concept, mcrawl):
	node_max=NODE_MAX
	leaves_max=LEAVES_MAX
	deep_max=DEEP_MAX
	
	no_of_leaves = float((mcrawl.get_num_concept_leaves(concept)+1)) 
	subsumer_no= len(list(set(concept.rparents()))) + 2

	num = float(no_of_leaves)/ float(subsumer_no)
	den = leaves_max
	#print  no_of_leaves,no_of_subsumers,num,den,float(num/den)
	ic = math.log10(float(num/den))
	ic = -1 * ic
	return ic
