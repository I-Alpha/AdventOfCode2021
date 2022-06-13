from copy import copy, deepcopy
from itertools import count, product
from collections import deque
import queue
import numpy as np

ma = np.ma


class Cell():
    def __init__(self, value: int, x = None, y = None, flashed=False,):
        self.value = value
        self.flashed = flashed
        self.x = x
        self.y = y

class Grid():
    def __init__(self, cell_grid):  
        self.cell_grid=deepcopy(cell_grid)
        self.flash_total=0
        self.flash_queue=[]
        self.flash_per_step=[]
        self.stepFlashNums=[]
        self.synced_at_step=False 
        self.synced=False 
    
    def increaseCellValuesBy(self, amount):
        for cell in self.cell_grid.flatten() :
            cell.value+=1
      
    def getNumberGrid(self):
       return np.array([[ y.value for y in x] for x in self.cell_grid] )
   
    def resetFlashed(self):
        for cell in self.cell_grid.flatten():
            cell.flashed=False
        self.flash_per_step.append(0)
        
        
    def printGrid(self):
        print(self.getNumberGrid())
        
    def flashCell(self, cell): 
       cell.value = 0 
       self.flash_total+=1
       cell.flashed = True
       adjecentCells = list(self.get_adjacent_cells(cell.x,cell.y))
       for x,y in adjecentCells:
            ncell = self.cell_grid[x,y]  
            if ncell.flashed:
               ncell.value = 0
            elif ncell.value < 9:
               ncell.value+=1   
            else:
                self.flashCell(ncell)
                
    def get_adjacent_cells(self, x_coords, y_coords):
        cell =  x_coords, y_coords
        _,size = self.cell_grid.shape
        for c in product(*(range(n-1, n+2) for n in (cell))):
            if c != cell and all(0 <= n < size for n in c):
                yield c 

    def checkFlashed(self,mode):
        flashed=False
        
        for i in self.cell_grid.flatten():
            if i.value > 9:
                self.flash_queue.append(i)
                flashed=True
        return flashed
    
def run_step(grid, step,verbose, mode="default"):     
    if verbose:
        print("\n\nBefore step -",step+1,"\n ")
        grid.printGrid()
    grid.resetFlashed()
    grid.increaseCellValuesBy(1)  
    if verbose:
        print("\nIncreaseCellValuesBy 1 step -",step+1,"\n ") 
        grid.printGrid()    
    while grid.checkFlashed(mode): 
        cell = grid.flash_queue.pop()
        grid.flashCell(cell) 
        grid.flash_per_step[step]+=1
        if verbose:
            print("\n\nFlashed step",step+1," Cell (" ,cell.x,", ",cell.y,") -\n" ) 
            grid.printGrid() 
        if mode =="sync":
            grid.synced =all(elem == 0 for elem in grid.getNumberGrid().flatten())
            
    return grid


def run_steps(grid,steps="sync",verbose=False):
    if steps == "sync":
        step = 0 
        while not grid.synced:
            run_step(grid,step,verbose,"sync")
            step+=1
        grid.synced_at_step=step
    else: 
        for i in range(steps):
            run_step(grid,i,verbose)
    return grid

cell_grid = np.array([[Cell(int(valy),ix,iy) for iy,valy in enumerate(valx)] for ix,valx in enumerate(open('day_11/input.txt', 'r').read().splitlines())]) 
 
grid = Grid(cell_grid)
grid = run_steps(grid,100) 
print(f"\nPart 1 Results Total Flashes: {grid.flash_total}\n")

Part2grid = Grid(cell_grid)
part2grid = run_steps(Part2grid,"sync") 
print(f"\nPart 2 Results  Synced at Step: {part2grid.synced_at_step}\n")

pass