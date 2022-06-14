from collections import deque
from copy import deepcopy 


allLinks ={}     

def isSmallCave (node):
    return node.lower() == node

def addLink (a, b): 
    if a in allLinks:
        allLinks[a].append(b) 
    else:
        allLinks[a]=[b]
        
_= [[[addLink(start,end) ,addLink(end,start)]  for start,end in [lines.split("-")]] for lines in open('day_12/input.txt', 'r').read().splitlines()]
            
def part1(): 
    
    def getPath(allLinks, visited, node):
            if (node == "end") :
                return 1
            discoveredPaths=0
            for linkedNode in allLinks[node]:
                if linkedNode not in visited:
                    if isSmallCave(linkedNode):
                        newVisited= visited + [linkedNode] 
                    else:
                        newVisited=visited
                    discoveredPaths  += getPath(allLinks, newVisited, linkedNode)
            return discoveredPaths
    return  getPath(allLinks, ["start"], "start")

def part2():  
    
    def getPath(allLinks, visited, node):
        
            def hasVisitedNode(visited, node):
                if (node == "start") :
                    return True
                return  (node in visited) and ("twice" in visited)

            def getVisitedNodes (visited, node):
                isSmallNode = isSmallCave(node)
                if not isSmallNode:
                    return visited
                if node in visited:
                    return visited + ["twice"]
                return  visited+ [node] 
            
            if  node == "end":
                return 1
            discoveredPaths=0
            for linkedNode in allLinks[node]:
                if not hasVisitedNode(visited, linkedNode): 
                    discoveredPaths  += getPath(allLinks, getVisitedNodes(visited, linkedNode), linkedNode)
            return discoveredPaths

    return getPath(allLinks, ["start"], "start")
 
    
paths1 = part1()
paths2 = part2()
print("\nPart 1", paths1)
print("\nPart 2", paths2)