
input = {};
f = open("day_02/input.txt", "r")
[depth, position] = (0,0) 

def pos(value) : 
    global position
    position += value

def depth(value) : 
    global depth
    if down-1 * value)
    depth += value
    
for x in f:
  [action,value] = x.replace('\n','').split(" "); 
  value =int(value);  
  switcher= {
      'forward': pos(value),
      'up' : depth(value),
      'down' : depth(() 
  } 
  value = switcher.get(action, "default")
print (depth, position)