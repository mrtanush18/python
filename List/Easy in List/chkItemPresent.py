list = []
list_size = int(input("\nEnter no. of elements: "))

for i in range(list_size):
    element = int(input())
    list.append(element)

print('\n',list)
toFind = int(input("\nEnter element to find: "))

for i in list:
    if toFind in list:
        flag = 1
    else:
        flag = 0

if(flag == 1):
    print('\n',toFind, " is present")
if(flag == 0):
    print('\n',toFind, " is not present")

# o/p:
# [1, 2, 3, 2, 5, 2]
# Enter element to find: 2
# 2  is present