
input = {};
f = open("day_03/input.txt", "r")

binaryNumbers = [(x.replace('\n','')) for x in f]
print(binaryNumbers)
    
gamma=0;
epsilon=0;
gammaBin = [];
for i in range(5):
    count=[0, 0]
    for binNum in binaryNumbers:
        count[int(binNum[i])] +=1;
    gammaBin[= count.index(max(count)))
