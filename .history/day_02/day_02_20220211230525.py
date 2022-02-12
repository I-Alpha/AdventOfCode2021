
input = {};
f = open("day_02/input.txt", "r")
[depth, position,aim] = (0,0,0) 

def pos(value,dr) : 
    global position
    position += value
    depth += aim * value
def depth_move(value) : 
    global depth
    if value < 0:
      aim -= value;
    else:
      aim += value;
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
 



