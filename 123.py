#initalisation

grid = [[1,1,1,0,0,0],
		[1,1,1,0,1,0],
		[0,0,0,0,0,0],
		[1,1,1,0,1,1],
		[1,1,1,0,1,1]]
		
goal=[2,0]
init = [4,3,0]	

forward=[[-1,0],
		 [0,-1,
		 [1,0],
		 [0,1]]

#forward_name = ['up','left','down','right']

cost = [2,1,0]
action = [-1,0,1]
action_name = ['R','#','L']

def show(Z):
	for i in range(len(Z)):
		print Z[i]

def ultimate_search():
	global grid,forward,forward_name,cost,action,action_name
	value = [[[999 for row in range(len(grid[0]))]for col in range(len(grid))],
			 [[999 for row in range(len(grid[0]))]for col in range(len(grid))],
			 [[999 for row in range(len(grid[0]))]for col in range(len(grid))],
			 [[999 for row in range(len(grid[0]))]for col in range(len(grid))]]
	
	check = True
			 
	while check is True:
		check = False
		
		x = init[0]
		y = init[1]
		theta = init[2]
		g =0
		open = [[0,x,y,theta]]
		
		while counter !=3:
			
			if x==goal[0] and y==goal[1] and theta==1:
				counter+=1
				
			else:
				open.sort()
				open.reverse()
				next = open.pop()
				x = next[1]
				y = next[2]
				theta = next[3]
				g = next[0]
				value[0][init[0]][init[1]] = 0		
				
				for i in action :
					x2 = x + forward[(theta+i)%4][0]
					y2 = y + forward[(theta+i)%4][1]
					theta2 = theta+i
					
					if x2>=0 and y2>=0 and x2<len(grid) and y2<len(grid[0]):
						if grid[x2][y2]==0:
							v2 = value[theta][x][y] + cost[i+1] 
							if v2<value[theta2][x2][y2]:
								value[theta2][x2][y2] = v2
								open.append([v2,x2,y2,theta2])
								
	show(value)
		
		
		
	
	
