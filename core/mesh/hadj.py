from constants import *
import math

"""
hadj ic calculator

"""
sdict = {}
avg = {}
rdict = {}

def hadj_mesh(concept, mcrawl):
	node_max=NODE_MAX
	leaves_max=LEAVES_MAX
	deep_max=DEEP_MAX
	subsumer_list = []
	depth_hyper = 0
	subsumer_l= list(set(concept.rparents())) + [concept]
	a = 0
	if avg.get(str(concept)) != None:
		a = avg.get(str(concept))
	else:
		for ancestor in subsumer_l:
			if str(ancestor).split(':')[1].strip() != '>':
				subsumer_list.append(ancestor)
		depth = 0
		for each_subsumer in subsumer_list:
			depth_hyper = depth_hyper + mcrawl.get_min_depth(each_subsumer)
	
		subsumer_no= len(subsumer_list) 
		a = (1.0/subsumer_no) * depth_hyper
		avg[str(concept)] = a

	avg_Depth =  a
	
	score = 0
	for each_sub in subsumer_list:
		s = 0
		if sdict.get(str(each_sub)) != None:
			s = sdict.get(str(each_sub))
		else:
		    ratio_dep_hypo = 0
		    no_of_direct_hyp = (list(set(each_sub.parents)))
		    each_sub_no_of_direct_hyper = []
		    for ancestor in no_of_direct_hyp:
			    if str(ancestor).split(':')[1].strip() != '>':
				    each_sub_no_of_direct_hyper.append(ancestor)
		    print each_sub_no_of_direct_hyper
		    for each_direct_hyper in each_sub_no_of_direct_hyper:
			    r = 0
			    if rdict.get(str(each_direct_hyper)) != None:
				    r = rdict.get(str(each_direct_hyper))
			    else:
			        depth = mcrawl.get_min_depth(each_direct_hyper)
			        no_of_hypo = len(list(set(each_direct_hyper.rchildren()))) + 1
			        r = (float(depth) / float(no_of_hypo))
			        rdict[str(each_direct_hyper)] = r
			        print each_direct_hyper,no_of_hypo
			    ratio_dep_hypo =  ratio_dep_hypo + r
		    hypo_each_subsum = len(list(set(each_sub.rchildren()))) + 1	
		    s = ratio_dep_hypo  * hypo_each_subsum
		    sdict[str(each_sub)] = s
		score  =  score +  s
		
	#no_of_leaves = float((mcrawl.get_num_concept_leaves(concept)+1)) 

	return score * avg_Depth
