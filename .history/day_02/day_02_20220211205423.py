
input = {};
f = open("day_02/input.txt", "r")
[depth, position] = (0,0) 

def pos(value) : 
    global position
    position = value + position 

def depth_move(value) : 
    global depth
    depth = value + depth 
    if depth < 0:
      depth = 0;
    
for x in f:
  [action,value] = x.replace('\n','').split(" "); 
  value =int(value);  
  switcher= {
      'forwad': pos(value),
      'up' : depth_move(-1 * value),
      'down' : depth_move(value) 
  } 
  value = switcher.get(action, "default")
print (depth * position)