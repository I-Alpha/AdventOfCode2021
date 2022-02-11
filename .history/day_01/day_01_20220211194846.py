from ast import For


input = [];
f = open("day_01/input.txt", "r")
for x in f:
   input.append(int(x.replace('\n',''))); 
  
##Part 1 
prev = input[0]; 
count = 0;
for i in range(1,len(input)):
    if input[i] > prev: 
        count += 1;
    prev = input[i]
    
print(count)

##Part 2

prev = input[0:3]; 
count = 0;
for i in range(4,len(input)):
    if input[i] > prev: 
        count += 1;
    prev = input[i:i+3]
    
 