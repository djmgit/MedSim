import math
from constants import ROOT_SNOMED_CONCEPT, ROOT_VAL_SNOMED

"""
pirro similarity model

"""

def filter(cs_set):
	temp=[]
	for cs in cs_set:
		s=str(cs)
		if s.split(':')[1].strip() != '>':
			temp.append(cs)
	return temp		

def our(term1, term2, concept1, concept2, ic_val, ontology, ic_model, util_library, graph):
	vcs = util_library.get_cs_set(concept1, concept2)

	if ontology == 'MESH':
		vcs = filter(vcs)

	s = 0

	for cs in vcs:
		ic = 0
		if ontology == 'SNOMEDCT' and cs == graph[ROOT_SNOMED_CONCEPT]:
			ic = 0
		else:
			ic = ic_model(cs, util_library)

		s=s+((ic/(float(ic_val[term1])-ic+1))+(ic/(float(ic_val[term2])-ic+1)))

	if len(vcs) != 0:
		s = float(s / len(vcs))

	return s
