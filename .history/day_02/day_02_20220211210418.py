
input = {};
f = open("day_02/input.txt", "r")
[depth, position] = (0,0) 

def pos(value) : 
    global position
    position += value

def depth_move(value) : 
    global depth
    depth += value  
    if depth < 0:
      depth = 0;
    
for x in f:
  [action,value] = x.replace('\n','').split(" "); 
  value =int(value);  
  if action ==
  if action ==
  if action == 'up'
      'forward': pos(value),
      'down' : depth_move(value),
      'up' : depth_move(-1 * value),
  } 
  value = switcher.get(action, "default")
print (depth * position)