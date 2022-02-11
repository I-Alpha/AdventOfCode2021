from ast import For


input = [];
f = open("input.txt", "r")
for x in f:
   input.append(int(x.replace('\n',''))); 
  
prev = input[0]; 
count = 0;

for i in range(1,len(input)):
    if input[i] > prev: 
        count += 1;
    prev = input[i]
print(count)