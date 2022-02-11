from ast import For


curr = input[0]; 
for i in range(1,len(input)):
    if input[i] > curr: 
        count += 1;
        curr = input[i];