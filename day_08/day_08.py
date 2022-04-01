from os import remove
from matplotlib.pyplot import table
import numpy as np
from pyparsing import line
import math




entry= open("day_07/input.txt", "r")

def getTotalUniqueDigits(data):
    totalNum=0
    for currLine in data.readlines():
        numArr=[0]*10
        signals,output=map(lambda x: x.split(' '), currLine.split(' | ')) 
        signals=[list(i) for i in signals]
        output=[list(i) for i in output]
        if output[-1][-1] == '\n':
            output[-1].remove('\n')

        digitsDict = { i:0 for i in range(10)}

        digitsDict[2]=1
        digitsDict[4]=4
        digitsDict[3]=7
        digitsDict[7]=8

        for i in output:
            numArr[digitsDict[len(i)]]+=1

        totalNum+=sum([numArr[i] for i in [1,4,7,8]])
    return totalNum
 
def decodeData(data):
    total=0 
    print("\n")
    for (indx,currLine) in enumerate(data.readlines()):
        totalNum=[]
        #remove "\n"
        outputOriginal=currLine.split(' | ')[1][:-1]
        signals,output=map(lambda x: x.split(' '), [currLine.split(' | ')[0],outputOriginal]) 
        signals=[set(i) for i in signals]
        output=[set(i) for i in output]
        
        uniqueDigitsDict = { i:0 for i in range(10)}
        uniqueDigitsDict[2]=1
        uniqueDigitsDict[4]=4
        uniqueDigitsDict[3]=7
        uniqueDigitsDict[7]=8

        codeDict = { i:'' for i in range(10)}
        
        for op in (signals+output):
            cnt=len(op)
            if cnt in [2,4,3,7]:
                codeDict[uniqueDigitsDict[cnt]]=op 
         
        digitDictIncomplete=True
        while digitDictIncomplete:
            for code in (signals+output): 
                segNum = len(code)
                if segNum == 6:
                    if codeDict[4].issubset(code):
                        codeDict[9]=code
                    if codeDict[9]!='' and codeDict[7].issubset(code) and codeDict[9] != code:
                        codeDict[0]=code
                    if codeDict[9]!='' and codeDict[0]!='' and codeDict[9]!=code  and  codeDict[0]!=code:
                        codeDict[6]=code
                if segNum == 5: 
                    if codeDict[3]!='' and code!=codeDict[3] and codeDict[9]!='' and len(codeDict[9].difference(code)) == 1:
                        codeDict[5]=code
                    if codeDict[6]!='' and len(code.difference(codeDict[6])) == 1:
                        codeDict[3]=code
                valArr=list(codeDict.values())
                if valArr.count('') == 1:
                   for cd in (signals+output):
                       if cd not in valArr:
                           codeDict[2]=cd 
                           break
                if '' not in (codeDict.values()):
                    digitDictIncomplete=False
                    break
               
        for (indx,(code)) in enumerate(output):
            if indx != 1 or indx != len(output):
                for (idx,(key,value)) in enumerate(codeDict.items()):
                    if value==code:
                        totalNum.append(key)                    
        entryOutput = int(''.join(str(e) for e in totalNum))  
        
        print(f" {indx} : {outputOriginal} : {entryOutput}")
        total+=entryOutput
        
    return total
   
# print(f"\nPart 1 : Total Unique Digits : {getTotalUniqueDigits(entry)}\n") 
print(f"\nPart 2 : Total Unique Digits : {decodeData(entry)}\n") 
    
