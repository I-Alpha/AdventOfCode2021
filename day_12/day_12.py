import numpy as np


class Path():
     def __init__(self,start,end):
         self.label = start + "->" + end
         self.start=start
         self.end=end
         self.traversedCount = 0
         self.isSmallCave =  end == end.lower()
    
allPaths =np.array([[Path(start,end) for start,end in [lines.split("-")]] for lines in open('day_12/input.txt', 'r').read().splitlines()]).flatten()

def printPaths(pathsArr):
    for paths in pathsArr: 
        for path in paths:
            print(path.label, end =", ") 
            
def getAvailablePaths(paths, path):
    return list(filter(lambda x : x.start == path.end, paths))
 

def traverse(paths):
    startPaths = list(filter(lambda x : x.start == "start",paths))
    discoveredPaths=[]
    count =  0  
    for start in startPaths:
        pathsForStart = [] 
        count2 =  0  
        queue=[start] 
        prevPath= start
        for path in paths:
            path.traversedCount  = 0 
        start.traversedCount +=1    
        pathsForStart.append([])
        discoveredPaths.append([])
        while len(queue) > 0:          
            currentPath =(queue.pop())
            print("\ncurrentPath:",currentPath.label)
            if currentPath.end ==  "end":
                allSmallCavesTraversed= all( x.traversedCount > 0 for x in list(filter(lambda x : x.isSmallCave, paths)))
                if not allSmallCavesTraversed:
                    continue
                else : 
                    pathsForStart[count].append(currentPath)  
                    currentPath.traversedCount +=1 
                    break
            else:
                 pathsForStart[count2].append(currentPath) 
                 currentPath.traversedCount +=1 
            for i in getAvailablePaths(paths, currentPath):
                if i not in queue and i != currentPath:
                    queue.append(i)
                currentPath.traversedCount +=1
            printPaths(pathsForStart) 
                
        discoveredPaths[count].append(pathsForStart)
        count +=1
        print("\n")
    
    return discoveredPaths

print("\n")
printPaths( traverse(allPaths))
