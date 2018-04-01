
"""
resnik similarity model

"""

def resnik(term1, term2, ic_val):

	sim_calc = float(ic_val[term1 + '&' + term2])
	
	return sim_calc
