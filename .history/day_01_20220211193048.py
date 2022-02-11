from ast import For


f = open("input.txt", "r")
for x in f:
  print(x) 
curr = input[0]; 
count = 0;

for i in range(1,len(input)):
    if input[i] > curr: 
        count += 1;
        curr = input[i];