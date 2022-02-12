
input = {};
f = open("day_03/input.txt", "r")

binaryNumbers = [(x.replace('\n','')) for x in f]
print(binaryNumbers)
    
  
for i in range(5):
    count = [0] * 2
    for binNum in binaryNumbers:
        binNum[i]