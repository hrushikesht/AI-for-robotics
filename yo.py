	

grid = [[0, 1, 0, 0, 0, 0],
		[0, 0, 0, 0, 1, 0],
		[0, 1, 0, 0, 1, 0],
		[0, 1, 0, 1, 0, 0],
		[0, 0, 0, 1, 0, 0]]
		
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

def search():
	global grid,init,goal,delta,delta_name,cost,heuristic,action
	
	action= [[-1 for row in range(len(grid[0]))] for col in range(len(grid))]
	#expand[0][0] = 0
	#action = expand
	
	
	path = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]
	
	step = 0
	
	checkboxer = grid
	checkboxer[0][0] = 1
	
	x = init[0]
	y = init[1]
	g =0
	f = g + heuristic[init[0]][init[1]]
	open =[[f, g , x , y]]
	check = True
	
	while(check is True):
		
		if x == goal[0] and y == goal[1]:
			print [g, x, y]
			check = False
			
		else:
			if len(open) == 0:
				print 'fail'
				check = False
			else:	
				open.sort()
				open.reverse()
				next = open.pop()
				x = next[2]
				y = next[3]
				g = next[1]
				f = next[0]
			
				for i in range(len(delta)):
					x2 = x + delta[i][0]
					y2 = y + delta[i][1]
				
					#print [g2,x2,y2]
				
					if x2>=0 and x2<len(grid) and y2>=0 and y2<len(grid[0]):
						if grid[x2][y2] == 0 and checkboxer[x2][y2] == 0:
							g2 = g + cost
							f2 = g2 + heuristic[x2][y2]
							open.append([f2,g2,x2,y2])
							checkboxer[x2][y2] = 1
							step = step + 1
							action[x2][y2] = i
							#expand[x2][y2] = step
							
	show(action)
	x = goal[0]
	y = goal[1]
	path[x][y] = '*'
	while x!=init[0] or y!= init [1]:
		print [x,y]
		x2 = x - delta[action[x][y]][0]
		y2 = y - delta[action[x][y]][1]
		path[x2][y2] = delta_name[action[x][y]]
		
		x=x2
		y=y2
	show(path)
	
			
					
					
search()

