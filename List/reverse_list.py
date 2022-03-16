# REVERSE LIST BY STARTING FROM LAST INDEX AND STORING IT IN NEW LIST
# To move towards front of list length - 1

list = [100,-56,5,6,7,8]
reversed_list = []

# size = int(input("Enter no. of elements in list"))

# print('Enter items in list')
# for i in range(size):
#     element = int(input())
#     list.append(element)
print('OG list: ',list)

length = len(list)

count = 0

for i in range(length):
    temp = list[length-1]
    reversed_list.append(temp)
    length = length - 1

    count = count + 1

print('Reversed list: ',reversed_list)

print('No. of iterations:',count)

# o/p:
# OG list: [100, -56, 5, 6, 7, 8]
# Reversed list:  [8, 7, 6, 5, -56, 100]
# No. of iterations: 6

    

