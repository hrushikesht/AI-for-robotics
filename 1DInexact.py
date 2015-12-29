p=[0.2,0.2,0.2,0.2,0.2]
pHit=0.6
pMiss=0.2
pExact=0.8
pUndershoot=0.1
pOvershoot=0.1

world=['green','red','red','green','green']
measure=['red','green']
motion=[1,1]

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
		s=pUndershoot*p[(k-U-1)%len(p)]
		s= s + pExact*p[(k-U)%len(p)]
		s=s + pOvershoot*p[(k-U+1)%len(p)]
		q.append(s)
	return q

p=sense(p,measure[0])
p=move(p,1)
p=sense(p,measure[1])
p=move(p,1)
	
print p

