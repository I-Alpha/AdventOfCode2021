from ast import For


  input.append();
f = open("input.txt", "r")
for x in f:
  input.append(); 
curr = input[0]; 
count = 0;

for i in range(1,len(input)):
    if input[i] > curr: 
        count += 1;
        curr = input[i];