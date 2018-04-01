def get_lca_snomed(concept1, concept2, snomed):

	term1_ancestor = []
	term2_ancestor = []
	common_ansector_all_ic = []
	d={}
	ca=[]
	for ancestor in list((concept1.ancestors_no_double())):
		term1_ancestor.append(ancestor)
	term1_ancestor = set(term1_ancestor)

	for ancestor in list((concept2.ancestors_no_double())):
		term2_ancestor.append(ancestor)	
	term2_ancestor = set(term2_ancestor)
	common_ansector = term1_ancestor.intersection(term2_ancestor)

	if common_ansector:
		ic_common_ansector = 0
		for each_common_ancestor in common_ansector:
			if each_common_ancestor == ROOT_SNOMEDCT:
				ic_common_ansector = 0.0
			else:
			    ic_common_ansector = get_ic_sanchez2011_snomed(each_common_ancestor)	
			common_ansector_all_ic.append(ic_common_ansector)

		common_ansector_all_ic.sort(reverse = True)	
		
		return common_ansector_all_ic[0]
