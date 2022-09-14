def getInstruction(inst):
    if "x" in inst:
        return { "axes":"x", "val":int(inst.replace("fold along x=",""))}
    if "y" in inst:
        return {"axes":"y", "val":int(inst.replace("fold along y=",""))} 
    
textInp = open('day_13/input.txt', 'r').read().splitlines()
ll = textInp.index("")
arr, instructions =  [ (int(x), int(y)) for x, y in list(map(lambda x: x.split(","), textInp[:ll]))], list(map(
   getInstruction, textInp[ll+1:]))


def checkPoint(inst,dotArr): 
    temp = []
    for point in dotArr:
        temp.append(point)
        if inst["axes"] == "y" and inst["val"] < point[1]:
                temp.remove(point)
                diff = (point[1] - inst["val"])*2
                if point[1] - diff >= 0:
                    new_point = (point[0], point[1] - diff)
                    if new_point not in temp:
                        temp.append(new_point) 
                        
        if inst["axes"] == "x" and inst["val"] < point[0]:
                temp.remove(point)
                diff = (point[0] - inst["val"])*2
                if point[0] - diff >= 0:
                    new_point = (point[0] - diff, point[1])
                    if new_point not in temp:
                        temp.append(new_point) 
    return list(set(temp))

 
def printDisplay(arr):
    maxY, maxX =  max([i for i,x in arr]),max([ x for i,x in arr])
    print(f"\nmaxX = {maxX} ,maxY = {maxY}\n")
    for rows in range(maxX+5):
        for cols in range(maxY+5):
            if (cols,rows) in arr:
                print("▓", end=' ')
            else:
                print(".", end=' ')
        print("\n")
        
def runPart1(arr):
    for i,inst in enumerate(instructions):  
        arr = checkPoint(inst,arr)
        print(f"cnt-{i} : ", len(arr))
    return arr

print("")
part1Arr = runPart1(arr)
        
printDisplay(part1Arr)