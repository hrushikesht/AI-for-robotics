#
#
#

#initialisation

grid = [[1, 1, 1, 0, 0, 0],
        [1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1]]
        
goal = [2, 0]
init = [4, 3, 0]  # first two elements are co-ordinates third one is direction

forward = [[-1, 0],   #up
           [0, -1],   #left
           [1, 0],    #down
           [0, 1]]   #right

forward_name = ['up','left','down','right']
cost = [2, 1 , 0]
action = [-1, 0, 1]
action_name = ['R','#','L']

value = [[[999 for row in range(len(grid[0]))] for col in range(len(grid))],
         [[999 for row in range(len(grid[0]))] for col in range(len(grid))],
         [[999 for row in range(len(grid[0]))] for col in range(len(grid))],
         [[999 for row in range(len(grid[0]))] for col in range(len(grid))]]
         
checkboxer = value
         
        
def turn_right(g,x,y,theta,forward,action):
    global cost
    x2 = x + forward[(theta-1)%4][0]
    y2 = y + forward[(theta-1)%4][1]
    theta2 = (theta + action[0]) % 4
    g2 = g + cost[0]
    if x2>=0 and x2<len(grid) and y2>=0 and y2<len(grid[0]):
        if grid[x2][y2]==0:
            return [g2,x2,y2,theta2]
        else:
            return 0
    else:
        return 0
        
def turn_left(g,x,y,theta,forward,action):
    global cost
    x2 = x + forward[(theta+1)%4][0]
    y2 = y + forward[(theta+1)%4][1]
    theta2  = (theta+action[2])%4
    g2 = g + cost[2]
    if x2>=0 and x2<len(grid) and y2>=0 and y2<len(grid[0]):
        if grid[x2][y2]==0:
            return [g2,x2,y2,theta2]
        else:
            return 0
    else:
        return 0
        
def go_straight(g,x,y,theta,forward,action):
    global cost
    x2 = x + forward[theta][0]
    y2 = y + forward[theta][1]
    g2 = g + cost[1]
    theta2 = theta
    if x2>=0 and x2<len(grid) and y2>=0 and y2<len(grid[0]):
        if grid[x2][y2]==0:
            return [g2,x2,y2,theta2]
        else:
            return 0
    else:
        return 0
        
#print go_straight(2,2,2,1,forward,action)


        
def path_planning(grid,goal,init,forward,forward_name,cost,action,action_name,value):
    
    # initialisation
    
    x0 = init[0]
    y0 = init[1]
    theta0 = init[2]
    g0 = 0
    open = [[g0,x0,y0,theta0]]
    check = 0
    while check != 3:
        
        #checking if goal is reached
        
        if x0==goal[0] and y0==goal[1] and theta0 == 1:
            check = check + 1
            
        else:
            #changing target grid
            open.sort()
            next = open.pop()
            x0 = next[1]
            y0 = next[2]
            theta0 = next[3]
            g0 = next[0]
            print next
            
            if grid [x0][y0] == 0 :
                yo = turn_right(g0,x0,y0,theta0,forward,action)
                if yo != 0:
                    open.append(yo)
                    if yo[0] < value[theta0][x0][y0]:
						value[theta0][x0][y0] = yo[0]
                   
                    
                yo = turn_left(g0,x0,y0,theta0,forward,action)
                if yo != 0:
                    open.append(yo)
                    if yo[0] < value[theta0][x0][y0]:
						value[theta0][x0][y0] = yo[0]
                    
                
                yo = go_straight(g0,x0,y0,theta0,forward,action)
                if yo != 0:
					print next
					open.append(yo)
					if yo[0] < value[theta0][x0][y0]:
						value[theta0][x0][y0] = yo[0]
    for i in range(len(forward)):
		for j in range(len(grid)):
			print value[i][j]
					
            
        
path_planning(grid,goal,init,forward,forward_name,cost,action,action_name,value)
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    
    
