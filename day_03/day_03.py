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
def OxygenRating(binaryNumbers,indx): 
    if len(binaryNumbers) == 1:
        return binaryNumbers[0];  
    count=[0, 0]
    for binNum in binaryNumbers:
        count[int(binNum[indx])] +=1;
    if (count[0]==count[1]):
        binTarget = '1';
    else:
        binTarget=str(count.index(max(count)));
    filteredArray =  [binNum for binNum in binaryNumbers if binNum[indx] == binTarget] ; 
    return OxygenRating(filteredArray,indx+1);


def C02Rating(binaryNumbers,indx): 
    if len(binaryNumbers) == 1:
        return binaryNumbers[0];  
    count=[0, 0]
    for binNum in binaryNumbers:
        count[int(binNum[indx])] +=1; 
    if (count[0]==count[1]):
        binTarget = '0';
    else:
        binTarget=str(count.index(min(count)));
    filteredArray =  [binNum for binNum in binaryNumbers if binNum[indx] == binTarget] ; 
    return C02Rating(filteredArray,indx+1);

oxygenGeneratorRating = int(OxygenRating(binaryNumbers,0),2);
C02GeneratorRating = int(C02Rating(binaryNumbers,0),2); 

print("C02GeneratorRating:", C02GeneratorRating, " oxygenGeneratorRating:", oxygenGeneratorRating, ", answer:" ,C02GeneratorRating*oxygenGeneratorRating)