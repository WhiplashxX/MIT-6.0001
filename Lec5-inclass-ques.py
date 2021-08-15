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
