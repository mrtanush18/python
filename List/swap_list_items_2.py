# Swap second last with first item

list = []
list_size = int(input("Enter size of list"))

print("Enter items in list")

for i in range(list_size):
    item = int(input())
    list.append(item)

print(list)

list[2], list[-7] = list[-7], list[2]

print(list)


# From back     , -10 , -9 , -8 , -7 , -6 , -5 , -4 , -3 , -2, -1
# Front             0 ,  1 ,  2,   3,   4,   5,   6,   7,   8,  9
# Ex.               1    2    3    4    5    6    7    8    9   10

# 0 is first , -1 is last