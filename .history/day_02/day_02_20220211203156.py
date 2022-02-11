
input = {};
f = open("day_02/input.txt", "r")
for x in f:
  [action,value] = x.replace('\n','').split(" "); 
  switcher=
  {
    key_1: value_1/method_1(),
    key_2: value_2/method_2(),
    key_3: value_3/method_3(), 
  key_n: value_n/method_n(),
  }
  key = N
  value = switcher.get(key, "default")