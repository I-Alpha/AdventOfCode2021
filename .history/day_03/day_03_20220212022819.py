
input = {};
f = open("day_03/input.txt", "r")

binaryNumbers = [(x.replace('\n','')) for x in f] 
    
def part1():
    gamma=0;
    epsilon=0;
    gammaBin = "";
    epsilonBin="";
    for i in range(len(binaryNumbers[0])):
        count=[0, 0]
        for binNum in binaryNumbers:
            count[int(binNum[i])] +=1;
        gammaBin+=str(count.index(max(count)));
        epsilonBin+=str(count.index(min(count)));
    gamma = int(gammaBin,2);
    epsilon = int(epsilonBin,2);
    print("\n\n\n" +str(gamma),epsilon)
    print(gamma*epsilon)

##part 2 
def part2():
    lifeSupportRating = 0;
    oxygenGeneratorRating = 0;
    CO2ScrubberRating = 0;
    for i in range(len(binaryNumbers[0])):
        count=[0, 0]
        for binNum in binaryNumbers:
            count[int(binNum[i])] +=1;
        gammaBin+=str(count.index(max(count)));

part1();
part2();