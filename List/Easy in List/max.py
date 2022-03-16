num = int(input("\nEnter no. of elements in list: "))
list = []

for i in range(num):
    element = int(input())
    list.append(element)
print('\n',list)

max_element = list[0]       # moved statement outside to reduce time complexity

for element in list:
    if(max_element<element): # > to find minimum element
        max_element = element
    
print('\nMax element is: ',max_element)


# o/p:

#  [-100, -90, -80, -10, -70, -60, -50]

# Max element is:  -10
    


