# Without using pow
list = [1,2,3]
cubeList = []
for value in list:
    cubeList.append(value*value*value)

print("No pow",cubeList)

# Using pow
list2 = [1,2,3]
cubeList2 = []
for values in list2:
    cubeList2.append(pow(values,3))
    
print("pow",cubeList2)

# o/p:
# No pow [1, 8, 27]
# pow [1, 8, 27]