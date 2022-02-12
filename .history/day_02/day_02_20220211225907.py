
input = {};
f = open("day_02/input.txt", "r")
[depth, position,aim] = (0,0) 

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
  
  if action == 'forward':pos(value), 
  if action == 'down': depth_move(value)
  if action == 'up': depth_move(-1 * value) 
   
print (depth * position)

##part2


