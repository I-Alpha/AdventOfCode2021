from matplotlib.pyplot import table
import numpy as np
from pyparsing import line
import math

data = list(map(lambda x: list(map(lambda y: int(y), x.split(","))),
            open("day_07/input.txt", "r")))[0]

def arithmetic_series(start, stop, step):
    number_of_terms = (stop - start) // step
    sum_of_extrema = start + (stop - step)
    return number_of_terms * sum_of_extrema // 2

def getFuelExpenditure(data, partTwo = False, verbose = False):
    lowestSum = 0
    for point in range(max(data)+1):    
        totalFuel = 0
        for num in data: 
            diff = (num-point)*-1 if (num-point) < 0 else (num-point)              
            if diff != 0:
                if partTwo:  
                    diff=arithmetic_series(0,diff+1,1)   
                totalFuel+=diff
            if verbose:
                print(f"Move from {num} to {point} : {diff}")
        
        if totalFuel < lowestSum or lowestSum < 1:
            lowestSum = totalFuel
            results = [totalFuel, point]
        if verbose:
            print(f"Total Fuel :{totalFuel}")    
            print("\n")
    return results
  
lowestFuelExpenditure = getFuelExpenditure(data)
print(f"\nPart1: Lowest fuel is at position {lowestFuelExpenditure[1]} using {lowestFuelExpenditure[0]} fuel\n")
 
lowestFuelExpenditure2 = getFuelExpenditure(data,partTwo=True)
print(f"Part2: Lowest fuel is at position {lowestFuelExpenditure2[1]} using {lowestFuelExpenditure2[0]} fuel\n")