
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
    print("\n\n\n" +str(gamma),epsilon);
    print(str(gamma*epsilon)+"\n\n\n");

##part 2 
    lifeSupportRating = 0;
    oxygenGeneratorRating = 0;
    CO2ScrubberRating = 0;
def part2(binaryNumbers,index): 
    if len(binaryNumbers) == 1:
        return binaryNumbers[0]; 
    for i in range(len(binaryNumbers[0])):
        count=[0, 0]
        for binNum in binaryNumbers:
            count[int(binNum[i])] +=1;
        binTarget=str(count.index(max(count)));
        filteredArray =  [binNum for binNum in binaryNumbers if binNum[i] == binTarget] ;
        print(filteredArray)
    return part2(filteredArray,index+1)
part1();
result = part2(binaryNumbers,1);
