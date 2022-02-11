
input = {};
f = open("day_02/input.txt", "r")
[depth, position] = (0,0) 

def pos(value) : 
    global position
    position = value + position 

def depth(value) : 
    global depth
    depth = value + depth 
    
for x in f:
  [action,value] = x.replace('\n','').split(" "); 
  switcher= {
      'forwad': pos(value),
      'up: depth(value),
      'down' :depth(value) 
  } 
  value = switcher.get(action, "default")
print 