from matplotlib.pyplot import table
import numpy as np
from pyparsing import line


data = list(map(lambda x: list(map(lambda y: int(y), x.split(","))),
            open("day_06/input.txt", "r")))[0]


def simulateFishCycles(initialData, steps=80,verbose= False): 
    fishTimerArr = dict({i:0 for i in range(9)}) 
    for j in initialData:
        fishTimerArr[j] += 1
    if verbose:
        print(fishTimerArr)
    for step in range(steps):
        fishTimerArr = updateFishArr(fishTimerArr) 
        if verbose:
            print(f"Step {step+1} : {sum(map(lambda x: x, fishTimerArr.values()))}")
    return sum(map(lambda x: x, fishTimerArr.values()))

def updateFishArr(fishTimerArr):
    fishesOnZero=0
    for keyNum in range(9):
        if keyNum==0:
            if fishTimerArr[keyNum] > 0:
                fishesOnZero=fishTimerArr[keyNum] 
                fishTimerArr[keyNum]=fishTimerArr[keyNum+1]
        else:
            fishTimerArr[keyNum-1]=fishTimerArr[keyNum] 
    fishTimerArr[8]=fishesOnZero
    fishTimerArr[6]+=fishesOnZero
    return fishTimerArr
 

print(f"\n total Fish after 80-days : {simulateFishCycles(data)}")

print(f"\ntotal Fish after 256-days : {simulateFishCycles(data,256)}\n")