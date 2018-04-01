"""
lin similarity model

"""

def lin(term1, term2, ic_val):
	
	sim_calc = float(2 * float(ic_val[term1 + "&" + term2])/(float(ic_val[term1]) + float(ic_val[term2])))

	return sim_calc