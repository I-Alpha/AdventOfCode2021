
input = {};
f = open("day_02/input.txt", "r")
[depth, position] = (0,0) 
position = value + position
for x in f:
  [action,value] = x.replace('\n','').split(" "); 
  switcher= {
      'forwad': (){position = value + position)},
      'up': value_2,
      'down': value_3  
  } 
  value = switcher.get(action, "default")
print 