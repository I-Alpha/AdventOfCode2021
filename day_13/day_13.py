 

import enum
from posixpath import split
from re import L

import numpy as np

class Cell():
    def __init__(self,x,y,on=False):
        self.x = int(x)
        self.y = int(y)
        self.label = str(x) + "," +str(y)
        self.on = on

def getXY_dimensions(dotList):
    maxY,maxX = 0,0
    for dot in dotList: 
        if dot.x > maxX: 
            maxX = dot.x 
        if dot.y > maxY: 
            maxY = dot.y
    return maxX+1,maxY+1

def formatGrid(grid, withCount = False):
    tempGrid = []
    count =0
    for r,row in enumerate(grid):
        tempGrid.append([])
        for cell in row:
            if cell.on:
                tempGrid[r].append("#")
                count +=1
            else:
                tempGrid[r].append(".")
    if withCount:
        return tempGrid, count
    return tempGrid
    
def getGrid(x,y,dotsList):
    grid=[]      
    labelist = [d.label for d in dotsList]
    for row in range (y):
        grid.append([])
        for col in range (x):
            cell = Cell(col,row)
            if cell.label in labelist:
                cell.on=True
            grid[row].append(cell)
    return grid

def foldGrid(grid,instruction,verbose=False):
    firstHalf, secondHalf=[],[]
    if verbose:
        print("\n") 
    axes,val = instruction.split("=")
    if axes == "y":
        firstHalf, secondHalf = grid[:int(val),:],grid[1+int(val):,:] 
        f_len= len(firstHalf)
        s_len = len(secondHalf)
        if verbose:
            print("\n",formatGrid(firstHalf))
            print("\n",formatGrid(secondHalf))
        startFrom = f_len - s_len 
        x = startFrom
        newCell = firstHalf
        while x < len(firstHalf):
            if x < s_len:
                for y, cell in enumerate(firstHalf[x]): 
                    if y < len(secondHalf[0]):
                        newCell[x][y].on = True if cell.on or secondHalf[::-1][x][y].on else False
                x+=1
    else:
        firstHalf, secondHalf  = grid[:,:int(val)],grid[:,1+int(val):]   
        f_len= len(firstHalf)
        s_len = len(secondHalf)
        if verbose:
            print("\n",formatGrid(firstHalf))
            print("\n",formatGrid(secondHalf)) 
        newCell = firstHalf
        for x,row in enumerate(firstHalf):
                if x < s_len:
                    for y, cell in enumerate(row): 
                        if y < len(secondHalf[0]):
                            newCell[x][y].on = True if cell.on or secondHalf[:,::-1][x][y].on else False
           
        
    return newCell             
    
lines = [lines for lines in open('day_13/input.txt', 'r').read().splitlines() if lines != ""]
dotsList= [Cell(line[0],line[1],False) for line in [line.split(",") for line in lines if "," in line ]] 
instructions = [line.split('fold along ')[1]  for line in [line for line in lines if "fold" in line ]]
maxX,maxY=getXY_dimensions(dotsList) 
grid =getGrid(maxX,maxY,dotsList) 

count={}
grid=np.array(grid)

for u,instruction in enumerate(instructions):
    grid=foldGrid(grid, instruction)
    fgrid,count[u] = formatGrid(grid,True)
    
print("\n",instructions[0])  
print("\n", fgrid)
print("\n Part 1", count[0]) 
