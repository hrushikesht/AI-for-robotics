# ----------
# User Instructions:
# 
# Create a function compute_value which returns
# a grid of values. The value of a cell is the minimum
# number of moves required to get from the cell to the goal. 
#
# If a cell is a wall or it is impossible to reach the goal from a cell,
# assign that cell a value of 99.
# ----------

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0]]
goal = [4,5]
cost = 1 # the cost associated with moving from a cell to an adjacent one

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

def compute_value(grid,goal,cost):
    
    #set variables
    
    operations=1
    path = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]
    value =[[99 for row in range(len(grid[0]))] for col in range(len(grid))]
    checkboxer = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
    print checkboxer
    check = True
    x = goal[0]
    y = goal[1]
    g = 0
    open=[[g,x,y]]
    while check is True :
        
        if len(open)==0: #check whether an expandable grid is available or not
            if operations == 0:
                check = False
                
        else :           #value assingning part
            open.sort()
            open.reverse()
            next = open.pop()
            x = next[1]
            y = next[2]
            g = next[0]
            operations = 0
            for i in range(len(delta)):
                x2 = x + delta[i][0]
                y2 = y + delta[i][1]
                g2 = g + cost
                if x2 >= 0 and x2<len(grid) and y2>=0 and y2<len(grid[0]):
                    if checkboxer[x2][y2] == 0 and grid[x2][y2] == 0:
                        open.append([g2,x2,y2])
                        value[x2][y2] = g2
                        checkboxer[x2][y2] = 1
                        operations = operations + 1
                        path[x2][y2] = delta_name[(i+2)%len(delta_name)]
    value[goal[0]][goal[1]] = 0
    path[goal[0]][goal[1]] = '*'
    for i in range(len(grid)):
        print value[i]
    for i in range(len(grid)):
        print path[i]
        
        
        
        
        
        
        
        

compute_value(grid,goal,cost)
