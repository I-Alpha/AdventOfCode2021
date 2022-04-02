from os import remove
import copy
from matplotlib.pyplot import table
import numpy as np
from pyparsing import line
import math


def getTotalUniqueDigits(data):
    totalNum = 0
    for currLine in data.readlines():
        numArr = [0]*10
        signals, output = map(lambda x: x.split(' '), currLine.split(' | '))
        signals = [list(i) for i in signals]
        output = [list(i) for i in output]
        if output[-1][-1] == '\n':
            output[-1].remove('\n')

        digitsDict = {i: 0 for i in range(10)}

        digitsDict[2] = 1
        digitsDict[4] = 4
        digitsDict[3] = 7
        digitsDict[7] = 8

        for i in output:
            numArr[digitsDict[len(i)]] += 1

        totalNum += sum([numArr[i] for i in [1, 4, 7, 8]])
    return totalNum


def getOutputTotal(data, verbose=False):
    
    def getUniqueDigitsDict():
        uniqueDigitsDict = dict()        
        uniqueDigitsDict[2] = 1
        uniqueDigitsDict[4] = 4
        uniqueDigitsDict[3] = 7
        uniqueDigitsDict[7] = 8
        return uniqueDigitsDict

    def decodeOutputs(totalNum, output, codeDict):
        for code in output:
            for (key, value) in codeDict.items():
                if value == code:
                    totalNum.append(key)
                    break

    def processInputLine(currLine):
        signals, output = list(map(lambda x: x.split(
                ' '), currLine.replace('\n', '').split(' | ')))
        signals = [set(items) for items in signals]
        output = [set(items) for items in output]
        return signals,output
    
    def getUniqueSignalCodePairs(signals, output, uniqueDigitsDict):
        codeDict = {i: '' for i in range(10)}
        for op in (signals+output):
            cnt = len(op)
            if cnt in [2, 4, 3, 7]:
                codeDict[uniqueDigitsDict[cnt]] = op
        return codeDict

    def matchSignalsToCode(signals, output, codeDict):
        digitDictIncomplete = True 
        while digitDictIncomplete:
            for code in signals+output:
                if code not in codeDict.values():
                    segNum = len(code)
                    if segNum == 6:
                        if codeDict[9]!='' and codeDict[6]!='' and len(code.intersection(codeDict[1])):
                            codeDict[0] = code
                        elif len(code.intersection(codeDict[4]))==4:
                            codeDict[9] = code
                        elif not codeDict[1].issubset(code):
                            codeDict[6] = code
                    elif segNum == 5:
                        if codeDict[1].issubset(code):
                            codeDict[3] = code
                        elif len(code.intersection(codeDict[4]))==3:
                            codeDict[5] = code
                        elif codeDict[3] != '' and codeDict[5] != '' and codeDict[3] != code and codeDict[5] != code:
                            codeDict[2] = code
                    
                    if '' not in (codeDict.values()):
                        digitDictIncomplete = False
                        break
 
    ### main process starts here
    total = 0
    uniqueDigitsDict = getUniqueDigitsDict()
    
    for currLine in data.readlines():
        totalNum = []
        
        signals, output = processInputLine(currLine)
 
        codeDict = getUniqueSignalCodePairs(signals, output, uniqueDigitsDict)

        matchSignalsToCode(signals, output, codeDict) 
                    
        decodeOutputs(totalNum, output, codeDict)
                
        entryOutput = int(''.join(str(e) for e in totalNum))
        if verbose:
            print("\n")
            print(f"{output} : {entryOutput}")
        total += entryOutput

    return total


##part1
entry = open("day_08/input.txt", "r")
print(f"\nPart 1 : Total Unique Digits : {getTotalUniqueDigits(entry)}") 

##part2
entry = open("day_08/input.txt", "r")
print(f"\nPart 2 : Total Unique Digits : {getOutputTotal(entry)}\n")
