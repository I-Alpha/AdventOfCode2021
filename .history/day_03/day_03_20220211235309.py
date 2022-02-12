
input = {};
f = open("day_03/input.txt", "r")

binaryNumbers = [(x.replace('\n','')) for x in f] 
    
gamma=0;
epsilon=0;
gammaBin = "";
epsilonBin="";
for i in range(5):
    count=[0, 0]
    for binNum in binaryNumbers:
        count[int(binNum[i])] +=1;
    gammaBin+=str(count.index(max(count)));
    epsilonBin+=str(count.index(min(count)));
gamma = int(gammaBin,2);
gamma = int(gammaBin,2);
print(gamma)