from os import remove
import copy
from matplotlib.pyplot import table
import numpy as np
from pyparsing import line 
import math 

ma=np.ma

data = [[int(x) for x in list(i)] for i in open('day_09/input.txt','r').read().splitlines()]
row_shape,col_shape=np.shape(data)

def get_mask():
    rowmask=np.array([False for i in range(row_shape)])
    return np.stack([rowmask for i in range(col_shape)],-1)
     

def getPossibleNeighbourCoords(lowest_point):
    neighbhours=[]
    if lowest_point[0]>0:
        neighbhours.append([lowest_point[0]-1,lowest_point[1]])
    if lowest_point[0]+1<row_shape:
        neighbhours.append([lowest_point[0]+1,lowest_point[1]])
    if lowest_point[1]>0:
        neighbhours.append([lowest_point[0],lowest_point[1]-1])
    if lowest_point[1]+1<col_shape:
        neighbhours.append([lowest_point[0],lowest_point[1]+1])
    return neighbhours

def get_lowpoint_masked_array(data, verbose=False):
    xmask = get_mask() 
    for rownum in range(row_shape):
        row_edge = [ False , '' ]
        if rownum in [0,row_shape-1]:
            row_edge = [True , ('upper' if rownum == 0 else 'lower')]
        for cellnum in range(col_shape):
            checks=[]
            cellVal = data[rownum][cellnum]        
            corner=[ False , '' ]
            cell_edge=[ False , '' ]
            if cellnum in [0,col_shape-1]:
                cell_edge =[True, ('left' if cellnum == 0 else 'right')]
            if cell_edge[0] and row_edge[0]:
                corner = [True, row_edge[1]+' '+cell_edge[1]]
            if corner[0]: 
                if corner[1] == 'upper left':
                        checks.append(cellVal<data[rownum+1][cellnum])
                        checks.append(cellVal<data[rownum][cellnum+1])                
                elif corner[1] == 'upper right': 
                        checks.append(cellVal<data[rownum+1][cellnum])
                        checks.append(cellVal<data[rownum][cellnum-1])
                elif corner[1] == 'lower left': 
                        checks.append(cellVal<data[rownum-1][cellnum])
                        checks.append(cellVal<data[rownum][cellnum+1])
                elif corner[1] == 'lower right':
                        checks.append(cellVal<data[rownum-1][cellnum])
                        checks.append(cellVal<data[rownum][cellnum-1])
            elif cell_edge[0]:
                checks.append(cellVal<data[rownum+1][cellnum])
                checks.append(cellVal<data[rownum-1][cellnum])
                if cell_edge[1] == 'left':
                    checks.append(cellVal<data[rownum][cellnum+1])    
                elif cell_edge[1] == 'right': 
                    checks.append(cellVal<data[rownum][cellnum-1]) 
            elif row_edge[0]:
                checks.append(cellVal<data[rownum][cellnum-1])
                checks.append(cellVal<data[rownum][cellnum+1])
                if row_edge[1] == 'upper':
                    checks.append(cellVal<data[rownum+1][cellnum])    
                elif row_edge[1] == 'lower': 
                    checks.append(cellVal<data[rownum-1][cellnum]) 
            else:
                checks.append(cellVal<data[rownum+1][cellnum])
                checks.append(cellVal<data[rownum-1][cellnum])
                checks.append(cellVal<data[rownum][cellnum-1])
                checks.append(cellVal<data[rownum][cellnum+1])
            xmask[rownum][cellnum] = not all(checks)
    if verbose:         
        print("\n")
        print("Mask: ", xmask)        

    return ma.masked_array(data,xmask,copy=True)

lowpoint_masked_array=get_lowpoint_masked_array(data)
valid_points = lowpoint_masked_array[~lowpoint_masked_array.mask]

                
visited = set()           

basins={}
lowest_points=[]
for rownum in range(row_shape):
    for cellnum in range(col_shape):
        if lowpoint_masked_array.mask[rownum][cellnum]==False:
            #begin depth first search marking as true
            lowest_points.append([rownum,cellnum])
            
def BFS(lowest_point_graph,lowest_point):
    queue=[]
    xmask=get_mask()
    queue.append(lowest_point)
    xmask[lowest_point[0]][lowest_point[1]]=True  
    dictID = f"{lowest_point[0]},{lowest_point[1]}"
    basins[dictID]=1
    
    while len(queue)>0:
        v  =  queue.pop()     
        neighbhours = getPossibleNeighbourCoords(v)        
        for neighbour in neighbhours:
            if xmask[neighbour[0]][neighbour[1]]==False:
                if lowest_point_graph[neighbour[0]][neighbour[1]]!=9:
                    queue.append(neighbour)
                    basins[dictID]+=1
                xmask[neighbour[0]][neighbour[1]]=True 

                
 
def getTotalbasinHeightsSum(basins):
    for point in lowest_points:
        BFS(lowpoint_masked_array.data,point)  
    basinHeights =list(basins.values())
    basinHeights.sort() 
    basinHeights.reverse() 
    return np.prod(basinHeights[:3])
   

print(f"\nPart 1 Result: {sum(valid_points)+len(valid_points)}")
print(f"Part 2 Results : {getTotalbasinHeightsSum(basins)}\n") 
               
               