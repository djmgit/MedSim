import math

"""
pirro similarity model

"""

def our(term1, term2, concept1, concept2, ic_val, ontology, ic_model, util_library):
	
	sim_calc = float(float(ic_val[term1+"&"+term2])/(float(ic_val[term1])+float(ic_val[term2])-float(ic_val[term1+"&"+term2])))

	return sim_calc
