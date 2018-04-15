import pronto
from MedSim.config import *

print 'Loading MeSH...'
mesh=pronto.Ontology(MESH_PATH)
print 'MeSH loaded'

class Mcrawl:

	

	def get_num_concept_leaves(self,concept):
		
		descendants=list(set(concept.rchildren()))
		leaves=[]
		for descendant in descendants :
			if len(descendant.children)==0:
				leaves.append(descendant)

		return len(list(set(leaves)))	

	def get_concept_leaves(self,concept):
		
		descendants=list(set(concept.rchildren()))
		leaves=[]
		for descendant in descendants :
			if len(descendant.children)==0:
				leaves.append(descendant)

		return list(set(leaves))		


	def	find_max_depth(self,concept):

		if len(concept.parents) == 0:
			return 0
		depth=max([self.find_max_depth(parent) for parent in concept.parents])
		return 1+depth


	def get_max_depth(self,concept):
		
		return self.find_max_depth(concept)+1


	def	find_min_depth(self,concept):


		if len(concept.parents) == 0:
			return 0
		depth=min([self.find_min_depth(parent) for parent in concept.parents])
		return 1+depth	

	def get_min_depth(self,concept):
		
		return self.find_min_depth(concept)+1

	def dist_subsumer_concept(self, concept, subsumer):
		if concept == subsumer:
			return 0
		if len(concept.parents) == 0:
			return 1000000
		dist = min([self.dist_subsumer_concept(parent, subsumer) for parent in concept.parents])
		return 1 + dist


	

	def get_lca(self,concept1,concept2):

		d={}
		ca=[]
		for ancestor in list(set(concept1.rparents())):
			d[ancestor]=1		

		for ancestor in list(set(concept2.rparents())):
			if d.get(ancestor) == 1:
				ca.append(ancestor)

		if len(ca) != 0:
			ca.sort(key = lambda x : self.get_max_depth(x))
			return	ca[len(ca)-1]
		return None	


	def get_mesh_depth(self):
		depth=-1
		temp=""
		for concept in mesh:
			#print concept.term
			d=self.get_min_depth(concept)
			if d>depth:
					
				depth=d
		print depth	

	def leaves_max(self):
		
		leaves=[]
		for concept in mesh:
			if len(concept.children)==0:
				leaves.append(concept)
		
		return len(set(leaves))

	def get_all_leaves(self):

		leaves=[]
		for concept in mesh:
			if len(concept.children)==0:
				leaves.append(concept)
		
		return list(set(leaves))


	def get_cs_set(self,concept1,concept2):
		d={}
		ca=[]
		for ancestor in list(set(concept1.rparents())):
			d[ancestor]=1		

		for ancestor in list(set(concept2.rparents())):
			if d.get(ancestor) == 1:
				ca.append(ancestor)

		
		if len(ca) == 0:
			return []

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
			an=list(set(i.rchildren()))
			for j in vcs:
				if j in an:
					fn=1
					break
			if fn!=1:
				vcs.append(i)		
					

		return vcs
''''
m=Mcrawl()
	
m.get_mesh_depth()
print m.leaves_max()
l=[]
'''

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



s=Mcrawl()
file=open('mesh_data.txt')
lines=file.read().split('\n')
multi=[]
#mf=open('multi.txt','a')
for line in lines:
	t1,t2=line.split()
	tr1,tr2=mesh[t1],mesh[t2]
	l=s.get_cs_set(tr1,tr2)
	print l
	

		
	#mf.write(st.strip()+'\n')
#mf.close()		
exit(0)
'''
'''
mcrawl=Mcrawl()

s=float(0.0)
for leaf in mcrawl.get_all_leaves():
		subsumer_no=len(list(set(leaf.rparents())))+1		
		s=s+float(1.0/subsumer_no)

print s		
'''
'''
s=Mcrawl()
leaves=s.get_all_leaves()
r=-1
for leaf in leaves:
	temp=len(list(leaf.rparents()))
	print temp
	if temp>r:
		r=temp
print r+1
'''	




	