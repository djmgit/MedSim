from pymedtermino import *

print 'Loading SNOMEDCT...'
from pymedtermino.snomedct import *
print 'SNOMEDCT loaded'

"""
Utility class for performing various operations

"""

class Scrawl:

	def get_num_parents(self,concept):

		return len(concept.parents)

	def get_num_children(self,concept):
		
		return len(concept.children)

	def get_num_acestors(self,concept):
	
		return len(list(concept.ancestors_no_double()))

	def get_num_descendants(self,concept):
		
		return len(list(concept.descendants_no_double()))

	def get_num_concept_leaves(self,concept):
		
		descendants=list(concept.descendants_no_double())
		leaves=[]
		for descendant in descendants :
			if len(descendant.children)==0:
				leaves.append(descendant)

		return len(leaves)	

	def get_concept_leaves(self,concept):
		
		descendants=list(concept.descendants_no_double())
		leaves=[]
		for descendant in descendants :
			if len(descendant.children)==0:
				leaves.append(descendant)

		return leaves		


	def	find_max_depth(self,concept):

		if len(concept.parents) == 0:
			return 0
		depth=max([self.find_max_depth(parent) for parent in concept.parents])
		return 1+depth


	def get_max_depth(self,concept):
		
		return self.find_max_depth(concept)	


	def	find_min_depth(self,concept):

		if len(concept.parents) == 0:
			return 0
		depth=min([self.find_min_depth(parent) for parent in concept.parents])
		return 1+depth	

	def get_min_depth(self,concept):
		
		return self.find_min_depth(concept)	

	def dist_subsumer_concept(self, concept, subsumer):
		if concept == subsumer:
			return 0
		if len(concept.parents) == 0:
			return 1000			
		dist = min([self.dist_subsumer_concept(parent, subsumer) for parent in concept.parents])
		return 1 + dist


	def get_lca(self,concept1,concept2):

		d={}
		ca=[]
		for ancestor in list(concept1.ancestors_no_double()):
			d[ancestor]=1		

		for ancestor in list(concept2.ancestors_no_double()):
			if d.get(ancestor) == 1:
				ca.append(ancestor)

		if len(ca) != 0:
			ca.sort(key = lambda x : self.get_max_depth(x))
			return	ca[len(ca)-1]
		return None	


	def get_snomed_depth(self):
		depth=-1
		temp=""
		for concept in list(SNOMEDCT[138875005].descendants_no_double()):
			#print concept.term
			d=self.get_min_depth(concept)
			if d>depth:
					
				depth=d
		print depth	

	def leaves_max(self):
		
		leaves=[]
		for concept in list(SNOMEDCT.all_concepts_no_double()):
			if len(concept.children)==0:
				leaves.append(concept)
		
		return len(leaves)

	def get_all_leaves(self):

		leaves=[]
		for concept in list(SNOMEDCT[138875005].descendants_no_double()):
			if len(concept.children)==0:
				leaves.append(concept)
		
		return (leaves)


	def get_cs_set(self,concept1,concept2):
		d={}
		ca=[]
		for ancestor in list(concept1.ancestors_no_double()):
			d[ancestor]=1		

		for ancestor in list(concept2.ancestors_no_double()):
			if d.get(ancestor) == 1:
				ca.append(ancestor)

		
		if len(ca) == 0:
			return None

		ca.sort(key = lambda x : self.get_max_depth(x))	

		temp=[]
		for i in range(len(ca)-1,-1,-1):
			temp.append(ca[i])

		vcs=[]
		vcs.append(temp[0])
		temp=temp[1:]
		fn=0
		for i in temp:
			fn=0
			an=list(i.descendants_no_double())
			for j in vcs:
				if j in an:
					fn=1
					break
			if fn!=1:
				vcs.append(i)		
					

		return vcs

#s=Scrawl()
#print s.get_snomed_depth()
# max_ic / batet calculation
'''
s=Scrawl()
leaves=s.get_all_leaves()
print len(leaves),'###############################'
r=-1
for leaf in leaves:
	temp=len(list(leaf.ancestors_no_double()))
	print temp
	if temp>r:
		r=temp
print r+1	
'''	
'''

print 'calculating cs set for each pair...'
def todigit(st):
	s=""
	st=str(st)
	return st[st.index('[')+1:st.index(']')]
	#for i in str(st):
		#if i.isdigit() == True:
			#s+=i
	#return s



s=Scrawl()
file=open('data.txt')
lines=file.read().split('\n')
multi=[]
mf=open('multi.txt','a')
for line in lines:
	t1,t2=line.split()
	tr1,tr2=SNOMEDCT[int(t1)],SNOMEDCT[int(t2)]
	l=s.get_cs_set(tr1,tr2)
	print l
	st=""
	for concept in l:
		st=st+todigit(concept)+' '

		
	mf.write(st.strip()+'\n')
mf.close()		
exit(0)
'''






		

'''
s=Scrawl()
print s.get_num_concept_leaves(SNOMEDCT[138875005])
'''



'''
print len(list(SNOMEDCT.all_concepts_no_double()))
s=Scrawl()
print s.leaves_max()







s=Scrawl()
#print s.leaves_max()
#print s.get_num_concept_leaves(SNOMEDCT[138875005])


l2=list(SNOMEDCT.all_concepts_no_double())
l1=list(SNOMEDCT.CORE_problem_list())
m=0
for i in l2:
		if i.is_in_core:
			print i,"True"
			m+=1
print m	

'''		

				






