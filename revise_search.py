grid = [[0, 1, 0, 0, 0, 0],
		[0, 0, 0, 0, 1, 0],
		[1, 1, 0, 1, 0, 0],
		[0, 1, 1, 0, 1, 0],
		[0, 0, 0, 0, 1, 0]]
		
heuristic = [[9, 8, 7, 6, 5, 4],
			 [8, 7, 6, 5, 4, 3],
			 [7, 6, 5, 4, 3, 2],
			 [6, 5, 4, 3, 2, 1],
			 [5, 4, 3, 2, 1, 0]]
		
init = [0, 0]
goal = [len(grid)-1,len(grid[0])-1]

delta = [[-1,0],
		 [0,-1],
		 [1,0],
		 [0,1]]
		 
delta_name=['^','<','v','>']

cost = 1

def show(Z):
	for i in range(len(Z)):
		print Z[i]

def find_value():
	global grid,delta,value,goal
	value = [[99 for row in range(len(grid[0]))] for col in range(len(grid))]
	action =  [[ -1 for row in range(len(grid[0]))] for col in range(len(grid))]
	policy = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]
	check = True
	
	while check is True:
		check = False
		print 1
		for x in range(len(grid)):
			for y in range(len(grid[0])):
				
				if goal[0] == x and goal[1] == y:
					if value[x][y]>0:
						value[x][y]=0
						check = True
				
				elif grid[x][y] == 0:
					for a in range(len(delta)):
						x2 = x+delta[a][0]
						y2 = y+delta[a][1]
						
						if x2>=0 and y2>=0 and x2<len(grid) and y2<len(grid[0]) and grid[x2][y2]==0:
							
							v2 = value[x2][y2] + cost
							
							if v2<value[x][y]:
								check = True
								value[x][y] = v2
								action[x][y] = a
								
	policy[goal[0]][goal[1]] = '*'
	for	x in range(len(grid)):
		for y in range(len(grid[0])):
			if action[x][y]!=-1:
				policy[x][y] = delta_name[action[x][y]]
	show(policy)
	show(value)
	
find_value()
				
