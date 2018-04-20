import math

"""
resnik similarity model

"""

def resnik(term1, term2, concept1, concept2, ic_val, ontology, ic_model, util_library, graph):

	sim_calc = float(ic_val[term1 + '&' + term2])
	
	return sim_calc
