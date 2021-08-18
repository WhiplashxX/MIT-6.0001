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

