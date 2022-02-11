from ast import For


input = [];
f = open("input.txt", "r")
for x in f:
   input.append(int(x.replace('\n',''))); 
  
curr = input[0]; 
count = 0;

for i in range(1,len(input)):
    if input[i] > curr: 
        count += 1;
    curr = input
print(count)