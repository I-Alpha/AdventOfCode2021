
input = {};
f = open("day_02/input.txt", "r")
for x in f:
  [action,value] = x.replace('\n','').split(" "); 
  