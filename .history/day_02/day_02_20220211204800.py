
input = {};
f = open("day_02/input.txt", "r")
 [depth, position] = (0,0) 

def pos(value) : 
    global position
    position += value

def depth(value, didr='') : 
    global depth
    if didr=='down':
      value = -1 * value;
    depth ;
    
for x in f:
  [action,value] = x.replace('\n','').split(" "); 
  value =int(value);  
  switcher= {
      'forward': pos(value),
      'up' : depth(value),
      'down' : depth(value, 'down')
  } 
  value = switcher.get(action, "default")
print (depth, position)