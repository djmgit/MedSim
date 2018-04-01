"""
Methods present in this file
calculates correlation

"""

import math

def fun1(x1,x,y1,y):
	z = 0
	z = ((x1 - x) * (y1 - y))

	return z
	
def fun2(x1,x):
	temp1 = math.pow(x1 - x , 2)

	return temp1

def get_corr(sim, ben):

	arr2_our_sim = []
	
	arr2_our_sim = sim
	arr1_mnc = ben
	
	p=0	
	for i in arr1_mnc:
		p = p + i
	
	length_arr1  = len(arr1_mnc)
	x_mean = float(p / length_arr1)
	
	s = 0
	for i in arr2_our_sim:
		s = s + i
	
	length_arr2 = len(arr2_our_sim)
	mean = s / length_arr2	
	y_mean = mean
	
	l = 30
	i = 0
	num  = 0
	den1 = 0
	den2 = 0	
	
	while i < length_arr1:
	
	
		num = num + fun1(arr1_mnc[i],x_mean,arr2_our_sim[i],y_mean)
		
		den1 = den1 + fun2(arr1_mnc[i],x_mean)
		den2 = den2 + fun2(arr2_our_sim[i],y_mean)
		
		i = i + 1
	
	
	den3 = den1 * den2
	den = math.sqrt(den3)	
	corr = num / den
	return corr
