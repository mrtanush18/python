dict = {1:'one', 2:'two', 3:'three'}
dict2 = {4:'four', 5:'five', 6:'six'}

dict.update(dict2)
print(dict)
# {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six'}

Lkeys = []
Lvalues = []

for keys,values in dict.items():
        Lkeys.append(keys)
        Lvalues.append(values)

print(Lkeys)
# [1, 2, 3, 4, 5, 6]
print(Lvalues)
# ['one', 'two', 'three', 'four', 'five', 'six']
new = {}

i = -1

while(i!= - len(Lkeys)-1):
    new.update({Lkeys[i] : Lvalues[i]})
    i = i - 1

print(new)

# o/p
# {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six'}
# [1, 2, 3, 4, 5, 6]
# ['one', 'two', 'three', 'four', 'five', 'six']
# {6: 'six', 5: 'five', 4: 'four', 3: 'three', 2: 'two', 1: 'one'}

# Try this program using for loop & range(start,stop,step)

# Try this program using reverse method
