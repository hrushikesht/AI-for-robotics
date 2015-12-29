#initialisation

path = [[0.,0.],
		[0.,1.],
		[0.,2.],
		[1.,2.],
		[2.,2.],
		[3.,2.],
		[4.,4.],
		[4.,3.],
		[4.,4.]]
		
def smooth(path,weight_data = 0, weight_smooth = 0.1 , tolerance = 0.000001):
	
	#newpath = [[0 for row in range(len(path[0]))] for col in range(len(path))]
	#for i in range(len(path)):
#		for j in range(len(path[0])):
#			newpath[i][j] = path[i][j]
	change = tolerance
	newpath = path		
	while change >= tolerance:
		change = 0.0
		
		for i in range(1,len(path)-1):
			for j in range(len(newpath[0])):
					
				aux = newpath[i][j]
				
				newpath[i][j] += weight_data*(path[i][j]-newpath[i][j])
				newpath[i][j] += weight_smooth*(newpath[i-1][j] + newpath[i+1][j] - (2*newpath[i][j]))
				
				change += abs(aux - newpath[i][j])
	return newpath
	
smooth1 = smooth(path)

for i in range(len(smooth1)):
	print smooth1[i]
					
					
