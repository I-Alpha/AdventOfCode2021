from matplotlib.pyplot import table
import numpy as np
from pyparsing import line

        
class Point:
    def __init__(self, x, y):
        # type: (Point, int, int) -> Point
        self.x = x
        self.y = y

class Line:
    def __init__(self, start, end):
        # type: (Line, Point, Point) -> Line
        self.start = start
        self.end = end


data = list(map(lambda x: (list(map(lambda y: tuple(map(int, y.split(','))),
            x.replace('\n', '').split(' -> ')))), open("day_05/input.txt", "r")))

lines = list(map(lambda x:
                 Line(
                     Point(x[0][0], x[0][1]),
                     Point(x[1][0], x[1][1])
                 ),
                 data
                 ))

vent_map = {}
numOfLines=len(lines) * 2

# for i in range(numOfLines):
#     for x in range(numOfLines):
#         vent_map[Point(x, i)] = 0

def printVentMap(vent_map, large = False):
    # type: (dict, bool) -> None
    values = list(vent_map.values())
    if large:
        for i in range(len(vent_map)):
            newline = ''
            if i % numOfLines/10 == 0:
                newline = '\n'
            value=values[i]
            print(f'{newline}   {int(value)}   ', end = '')
    else:
        print("\n\n",np.reshape(values,(numOfLines,numOfLines)))
        
def update(p: Point):  
    if vent_map.get(f'{p.x},{p.y}') is not None:
        vent_map[f'{p.x},{p.y}'] = vent_map[f'{p.x},{p.y}'] + 1
    else:
        vent_map[f'{p.x},{p.y}'] = 1      

def updateVentMap(line, partTwo = False ):
    
    def getRangeX():
        stepX = 1 if line.end.x > line.start.x else -1
        return range(line.start.x, line.end.x + stepX, stepX)

    def getRangeY():
        stepY = 1 if line.end.y > line.start.y else -1
        return range(line.start.y, line.end.y + stepY, stepY)

    if line.start.x == line.end.x:
        for py in getRangeY():
            update(Point(line.start.x, py))
    elif line.start.y == line.end.y:
        for px in getRangeX():
            update(Point(px, line.start.y))            
    elif partTwo:
        for (px, py) in zip(getRangeX(), getRangeY()):
            update(Point(px, py))

print("\n")
 

def getOverlappingVents(partTwo = False, verbose = False, withMap = False, large=False):
    for v, i in enumerate(lines):
        if verbose:
            print(f"\nline {v+1} : ({i.start.x},{i.start.y}) -> ({i.end.x},{i.end.y})")
        if withMap:
            printVentMap(vent_map,large)
        updateVentMap(i, partTwo)
    results = [i for i in vent_map if vent_map[i] > 1]
   
    return results


print(f"Overlapping lines p1 : {len(getOverlappingVents())}\n")

vent_map = {}
print(f"Overlapping lines p2 : {len(getOverlappingVents(True))}\n")
# print("\n",data,"\n\n", mask,"\n")
