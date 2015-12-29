
a=0.05
pHit=0.6
pMiss=0.2
pExact=0.8
pUndershoot=0.1
pOvershoot=0.1
sensor_right=0.7
p_move=0.8


p=[[a,a,a,a,a],
   [a,a,a,a,a],
   [a,a,a,a,a],
   [a,a,a,a,a],
   [a,a,a,a,a]]
   
colours=[['red','green','green','red','red'],
		 ['red','red','green','red','red'],
		 ['red','red','green','green','red'],
		 ['red','red','red','red','red']]
	
measure=['green','green','green','green','green']

motion=[[0,0],[0,1],[1,0],[1,0],[0,1]]

def sense(p,Z):
	row1=[]
	row2=[]
	row3=[]
	row4=[]
	w=[]
	q=[row1,row2,row3,row4]
	for i in range(4):
		for j in range(5):
			hit=( (Z==colours[i][j]))
			q[i].append(p[i][j]*(hit*sensor_right+(1-hit)*(1-sensor_right)))
	for i in range(4):
		w.append(sum(q[i]))	
	for i in range(4):
		for j in range(5):
			q[i][j]=q[i][j]/sum(w) 
	return q
	
def move(p,U):
	row1=[]
	row2=[]
	row3=[]
	row4=[]
	q=[row1,row2,row3,row4]
	w=[]
	
	if U[1]==1:
		for i in range(4):
			for j in range(5):
				horsum= p_move*p[i][(j-U[1])%5]
				horsum=horsum+ (1-p_move)*p[i][j%5]
				q[i].append(horsum)
	if U[0]==1:
		for k in range(5):
			for l in range(4):
				versum=p_move*p[(l-U[0])%4][k]
				versum=versum+(1-p_move)*p[l][k]
				q[l].append(versum)
	if U[0]==0:
		if U[1]==0:
			q=p
	for i in range(4):
		w.append(sum(q[i]))
	for o in range(4):
		for c in range(5):
			q[o][c]=q[o][c]/sum(w)
	return q
	

for i in range(len(measure)):
	p=move(p,motion[i])
	p=sense(p,measure[i])
print p
			
			
	
	
	
	
	
				
