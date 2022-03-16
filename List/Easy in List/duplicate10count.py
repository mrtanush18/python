# Print how many times number is repeating ?

list = [5,10,10,12,12,28,10]
count = 0

for i in list:
    if i == 10:
        count = count + 1

print(count)

# o/p:
# 3

# _____________________________________________________________
# Using method

list2 = [5,10,10,12,12,28,10]
x = 12

print(list2.count(x))

# o/p:
# 2