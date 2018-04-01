"""
montserrat batet similarity model

"""

def batet(term1, term2, ic_val):
	# Alternatice way required to set max_ic
	
	max_ic = 128
	sim_calc = -1*math.log10(float((float(ic_val[term1])+float(ic_val[term2])-2*float(ic_val[term1+"&"+term2])+1)/(2*max_ic)))

	return sim_calc