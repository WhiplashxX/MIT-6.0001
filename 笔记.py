L1 = ['re']
L2 = ['mi']
L3 = ['do']
L4 = L1 + L2
L3.extend(L4)
L3.sort()
del(L3[0])
L3.extend(['fa','la'])   #['mi', 're', 'fa', 'la']。 mutate list with L.extend(some_list)
#L3.append(['fa','la'])  #['mi', 're', ['fa', 'la']]。add elements to end of list with L.append(element)


#('cloudy'), ('cold',) with a commas:tuple ; without:string
------------------------

assert not len(grades)==0,'no grades data'
#not len(grades)==0 :means what the function expects
------------------------
__add__(self, other) -> self + other
__sub__(self, other) -> self - other
__eq__(self, other)  -> self == other
__lt__(self, other)  -> self < other
__len__(self)        -> len(self)
__str__(self)        -> print self
------------------------
if c in 'abcdefghijklmnopqrstuvwxyz':#judge a char is whether a letter or not
  
  
-----------------------
DEFAULT ARGUMENTS
def set_name(self,newname=""):
  self.name = newname
#we can pass no parameter in,that's OK

----------------------
class variables are typically defined inside the class defintion but outside the __init__
#is shared among all instances

----------------------
def linear_search(L,e):
  found = False
  for i in range(len(L)):
    if e==L[i]:
      found = True
  return found
#speed up a little by returning True here,but speed up doesn't impact worst case 
#the order of growth captures what's the worst case behavior
