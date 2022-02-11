
input = {};
f = open("day_02/input.txt", "r")
[depth, position] = (0,0) 

def pos(value) : 
    global position
    position = value + position 

def pos(value) : 
    global position
    position = value + position 
    
for x in f:
  [action,value] = x.replace('\n','').split(" "); 
  switcher= {
      'forwad': pos(value),
      'up':f pos(value),
      'down': value_3  
  } 
  value = switcher.get(action, "default")
print 