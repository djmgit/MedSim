import math

"""
jian similarity model

"""

def jian(term1, term2, concept1, concept2, ic_val, ontology, ic_model, util_library):

	sim_calc=float(ic_val[term1])+float(ic_val[term2])-(2*float(ic_val[term1+'&'+term2]))
	sim_calc=1-float(sim_calc/2.0)

	return sim_calc