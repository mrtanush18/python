num = int(input("size of list"))

list = []

for i in range(num):
    element = int(input())
    list.append(element)

list[0],list[-1] = list[-1],list[0]

# Long way to swap 1st & last items in list:
# length = len(list)
# temp1 = list[0]
# temp2 = list[length-1]

# list[length-1] = temp1
# list[0] = temp2

print(list)

