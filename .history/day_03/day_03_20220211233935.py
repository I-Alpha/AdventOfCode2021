
input = {};
f = open("day_03/input.txt", "r")

binaryNumbers = [(x.replace('\n','')) for x in f]
print(binaryNumbers)
    
gamma=0
epsilon=0
for i in range(5):
    for binNum in binaryNumbers:
        count[binNum[i]] +=1
    gammaBin[i] = max(count[i])
