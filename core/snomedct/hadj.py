from constants import *

"""
hadj ic calculator

"""
def hadj_snomed(concept, snomed):
	node_max=NODE_MAX
	leaves_max=LEAVES_MAX
	deep_max=DEEP_MAX
	subsumer_list = []
	depth_hyper = 0
	subsumer_list= list(set(concept.ancestors_no_double())) + [concept]

	depth = 0
	for each_subsumer in subsumer_list:
		depth_hyper = depth_hyper + snomed.get_min_depth(each_subsumer)

	subsumer_no= len(subsumer_list) 

	avg_Depth =  (1.0/subsumer_no) * depth_hyper
	
	score = 0
	for each_sub in subsumer_list:
		ratio_dep_hypo = 0
		
		each_sub_no_of_direct_hyper = []
		each_sub_no_of_direct_hyper = (list(set(each_sub.parents)))
		
		for each_direct_hyper in each_sub_no_of_direct_hyper:
			depth = snomed.get_min_depth(each_direct_hyper)
			no_of_hypo = len(list(set(each_direct_hyper.descendants_no_double())))
			#print each_direct_hyper,no_of_hypo
			ratio_dep_hypo =  ratio_dep_hypo + (float(depth) / float(no_of_hypo))
		hypo_each_subsum = len(list(set(each_sub.descendants_no_double())))	
		score  =  score +  ratio_dep_hypo  * hypo_each_subsum

	return score * avg_Depth
