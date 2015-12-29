#initialisation

grid = [[0,0,0,0],
		[0,0,0,0],
		[0,0,0,0],
		[0,1,1,0]]
		
goal = [0,len(grid[0])-1]

delta = [[-1,0],
		 [0,-1],
		 [1,0],
		 [0,1]]
		 
delta_name=['^','<','v','>']

success_prob = 0.5
collision_cost=100

value=[[1000 for row in range(len(grid[0]))] for col in range(len(grid))]
policy = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]

def show(Z):
	for i in range(len(Z)):
		print Z[i]

def ultimate_search():
	global grid,policy,value,collision_cost,sccess_prob,delta,delta_name,goal
	operations = [[-1 for row in range(len(grid[0]))] for col in range(len(grid))]
	check = False
	
	while check is False:
		
		check = True
		
		for x in range(len(grid)):
			for y in range(len(grid[0])):
				if x==goal[0] and y==goal[1]:
					if value[x][y]>0:
						value[x][y] = 0
						check = False
				
				elif grid[x][y]==0:
					for i in range(len(delta)):
						x2 = x + delta[i][0]
						y2 = y + delta[i][1]
						
						if x2>=0 and y2>=0 and x2<len(grid) and y2 <len(grid[0]):
							#if grid[x2][y2] == 0:
								if grid[x2][y2] == 0:
									v2_1 = success_prob*value[x2][y2]
								else:
									v2_1 = success_prob*100
									
								x_R = x + delta[(i-1)%4][0]
								y_R = y + delta[(i-1)%4][1]
								x_L = x + delta[(i+1)%4][0]
								y_L = y + delta[(i+1)%4][1]
								
								if x_R<0 or y_R<0 or x_R>=len(grid) or y_R>=len(grid[0]) or grid[x_R][y_R]==1:
									v2_2 = (success_prob/2.0)*100
								else:
									v2_2 = (success_prob/2.0)*value[x_R][y_R]
									
								if x_L<0 or y_L<0 or x_L>=len(grid) or y_L>=len(grid[0]) or grid[x_L][y_L]==1:
									v2_3 = (success_prob/2.0)*100
								else:
									v2_3 = (success_prob/2.0)*value[x_L][y_L]
									
								v2 = v2_1 + v2_2 + v2_3 + 1
								
								if v2<value[x][y]:
									value[x][y] = v2
									operations[x][y] = i
									check = False
	
	policy = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]
	for x in range(len(grid)):
		for y in range(len(grid[0])):
			if grid[x][y] == 0:
				policy[x][y] = delta_name[operations[x][y]]		
	policy[goal[0]][goal[1]] = '*'						
	show(value)
	show(policy)
	
ultimate_search()
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
