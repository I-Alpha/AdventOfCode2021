from argon2 import Type
import numpy as np

ma = np.ma

class Cell():
    def __init__(self, value: int, x = None, y = None, flashed=False,):
        self.value = value
        self.flashed = flashed
        self.x = x
        self.y = y

class Grid():
    def __init__(self, cell_grid=False): 
        self.grid_shape=np.shape(cell_grid)
        self.cell_grid=[]
        self.flash_queue=[] 
        self.flash_total=0
        self.stepFlashNums=[]
        self.synchroniousFlashStep=False
        self.get_cell_grid(cell_grid)

        
    def get_cell_grid(self,cell_grid):
        self.cell_grid= cell_grid 

    def get_grid_dict(self):
        grid_dict=[]
        for i in range(self.grid_shape[0]):
            for x in range(self.grid_shape[1]):
                  self.cell_grid[i][x].x,self.cell_grid[i][x].y=i,x 
                  grid_dict.append((i,x))
        return grid_dict
    
    def get_vals(self):
        vmap = []
        for i in range(self.grid_shape[0]):
            vmap.append([])
            for cell in self.cell_grid[i]:
                vmap[i].append(cell.value)
        return np.array(vmap)

    def increase_energy_by(self,num=1):
        for row in self.cell_grid:
            for cell in row: 
                if not cell.flashed:
                    cell.value+=num
                
    def get_mask(self):
        rowmask=np.array([False for i in range(self.grid_shape[0])])
        return np.stack([rowmask for i in range(self.grid_shape[1])],-1) 
    
    def check_flashes(self):
        for row in self.cell_grid:
            for cell in row:
                if cell.value>9:
                    cell.value=0
                    if not cell.flashed:
                        self.flash_queue.append(cell)
                        cell.flashed=True
                        self.flash_total+=1
                        self.flash_per_step+=1 
                        
    def reset_flashed(self):
        for row in self.cell_grid:
            for cell in row:
                cell.flashed=False 
                
    def get_adjacent_indices(self, x_coord, y_coord): 
        result=[]
        for x,y in [(x_coord+i,y_coord+j) for i in (-1,0,1) for j in (-1,0,1) if i != 0 or j != 0]:
            if (x,y) in self.get_grid_dict():
                result.append((x,y))
        return result
    
def step(main_grid: Grid):
    main_grid.flash_per_step=0   
    main_grid.increase_energy_by(1)                
    main_grid.check_flashes()
    while len(main_grid.flash_queue) > 0:
            cell=main_grid.flash_queue.pop(0)
            neighbhours=main_grid.get_adjacent_indices(cell.x,cell.y)
            for neighbour in neighbhours:      
                neighbourCell=main_grid.cell_grid[neighbour[0]][neighbour[1]]
                if not neighbourCell.flashed:
                    neighbourCell.value+=1
                    main_grid.check_flashes()   
    main_grid.stepFlashNums.append(main_grid.flash_per_step)
    main_grid.reset_flashed()
    step(main_grid.flash_queue)

def run_step(verbose, grid, x):
    step(grid) 
    if grid.stepFlashNums[x] == grid.grid_shape[0]*grid.grid_shape[1] and not grid.synchroniousFlashStep:
        grid.synchroniousFlashStep=x
    if verbose:
        print(f"\nAfter step {x+1}:\n{(grid.get_vals())}\nFlash count: {grid.stepFlashNums[x]}")
        
def run_steps(total_steps=False, verbose=False): 
    grid = Grid(data) 
    if verbose:
        print(f"\nBefore any steps:\n{(grid.get_vals())}")
    if total_steps:
        for x in range(total_steps):
            run_step(verbose, grid, x) 
            if verbose:
                print(f"\nCurrent Flashes Recorded: {grid.stepFlashNums}")
    else: 
        x=0
        while not grid.synchroniousFlashStep:
            run_step(verbose, grid, x) 
            x+=1
            if verbose:
                print(f"\nCurrent Flashes Recorded: {grid.stepFlashNums}")
    
    return [sum(grid.stepFlashNums),grid]

data = np.array(
    list(map(lambda x: np.array(list(map(lambda y: Cell(int(y)), x))), 
            [list(i) for i in open('day_11/input.txt', 'r').read().splitlines()]
    )))

for row in range(len(data)):
    for cell in range(len(data[row])):
        data[row][cell].x = row
        data[row][cell].y = cell
        
total_flashes,grid_100_steps=run_steps(100)
print(f"\nPart 1 Results Total Flashes: {total_flashes}\n")

total_flashes_synced,grid_synced=run_steps()
print(f"Part2 First Synchronius flashing at step: {total_flashes_synced, grid_synced.synchroniousFlashStep}\n")