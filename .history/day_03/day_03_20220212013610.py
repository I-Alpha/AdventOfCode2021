
input = {};
f = open("day_03/input.txt", "r")

binaryNumbers = [(x.replace('\n','')) for x in f] 
   
   
def (binaryNumbers) 
gamma=0;
epsilon=0; 
for i in range(len(binaryNumbers[0])):
    count=[0, 0]
    for binNum in binaryNumbers:
        count[int(binNum[i])] +=1;
    popBinNum=count.index(max(count));

#     epsilonBin+=str(count.index(min(count)));
# gamma = int(gammaBin,2);
# epsilon = int(epsilonBin,2);
# print(gamma,epsilon)
# print(gamma*epsilon)

##part 2 
lifeSupportRating = 0;
oxygenGeneratorRating = 0;
cO2ScrubberRating = 0;
bitCriteria = 0;

