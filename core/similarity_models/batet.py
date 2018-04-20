from constants import MAX_IC_SNOMED, MAX_IC_MESH
import math

"""
montserrat batet similarity model

"""

def batet(term1, term2, concept1, concept2, ic_val, ontology, ic_model, util_library, graph):

	# select max_ic according to ontology
	max_ic = MAX_IC_SNOMED
	if ontology == 'MESH':
		max_ic = MAX_IC_MESH

	sim_calc = -1*math.log10(float((float(ic_val[term1])+float(ic_val[term2])-2*float(ic_val[term1+"&"+term2])+1)/(2*max_ic)))

	return sim_calc
