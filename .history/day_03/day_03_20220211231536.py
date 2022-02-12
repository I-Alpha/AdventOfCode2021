
input = {};
f = open("day_03/input.txt", "r")

   
for x in f:
  [action,value] = x.replace('\n','').split(" "); 
  value =int(value);  