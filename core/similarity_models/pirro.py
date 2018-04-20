import math

"""
pirro similarity model

"""

def pirro(term1, term2, concept1, concept2, ic_val, ontology, ic_model, util_library, graph):
	
	sim_calc = float(float(ic_val[term1+"&"+term2])/(float(ic_val[term1])+float(ic_val[term2])-float(ic_val[term1+"&"+term2])))

	return sim_calc
