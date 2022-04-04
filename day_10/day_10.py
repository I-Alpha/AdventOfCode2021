data = [list(i) for i in open('day_10/input.txt', 'r').read().splitlines()] 

symbolStates = {
    '(': [3, ')'],
    '[': [57, ']'],
    '{': [1197, '}'],
    '<': [25137, '>'],
} 

symbolStates2={
    ')': 1 ,
    ']': 2 ,
    '}': 3 ,
    '>': 4 
}

def calculateScore(symbols):
    total=0
    for symbol in symbols:
        total=(total*5)+symbolStates2[symbol]
    return total

def getResults(data):
    
    total=0
    closingArr=[] 
    totalList=[]
    closedBrackets=list([i[1] for i in  symbolStates.values()])
    openBrackets=list([i for i in  symbolStates.keys()])
    bracketPairs={open:close for (open,close) in zip(openBrackets,closedBrackets)}
    closed_val_Pairs={close:val[0] for (close,val) in zip(closedBrackets, symbolStates.values())} 
    
    for line in data: 
        queue=[] 
        notCorrupted=True
        for symbol in line: 
            if symbol in openBrackets:
                queue.append(symbol)
            else:
                if len(queue)>0:
                    if bracketPairs[queue[-1]]!=symbol:                           
                            total+=closed_val_Pairs[symbol]
                            notCorrupted=False
                            break 
                    queue.pop()   
        if notCorrupted: 
            closingArr.append(list(queue))

    for symb_set in closingArr:
        symb_set.reverse()
        symb_set=list(map(lambda x: bracketPairs[x],symb_set))
        totalList.append(calculateScore(symb_set))

    totalList.sort()
    totalList.reverse()
    tllen= len(totalList) 
    middleScore=totalList[int(((tllen/2)+0.5)-1)]
    return total,middleScore



total, middleScore = getResults(data) 

print(f"\nPart 1 Result : {total}") 
print(f"\nPart 2 Result : {middleScore}\n") 