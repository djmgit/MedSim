import math

"""
meng and gu similarity model

"""

def menggu(term1, term2, ic_val, ontology, ic_model):
	sim_calc = float(2*float(ic_val[term1+"&"+term2])/(float(ic_val[term1])+float(ic_val[term2])))
	sim_calc = math.exp(sim_calc) - 1.0

	return sim_calc
