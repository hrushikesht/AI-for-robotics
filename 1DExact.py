p=[0,1,0,0,0]
pHit=0.6
pMiss=0.2

world=['green','red','red','green','green']
measure=['red']
Z='red'
def sense(q,Z):
	q=[]
	for i in range(len(p)):
		hit=(Z==world[i])
		q.append(p[i]*(hit*pHit+(1-hit)*pMiss))
	S=sum(q)
	for j in range (len(p)):
		q[j]=q[j]/S
	return q

#for i in range(len(measure)):
	#p=sense(p,measure[i])

def move(p,U):
	q=[]
	for k in range(len(p)):
		q.append(p[(k-U)%len(p)])
	return q

		
print sense(p,Z)
