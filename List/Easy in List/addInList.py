# 1
list = []
list.append(1)
list.append(2)
list.append(3)

print(list)

# 2
for i in range(1,4):   # (1,4) means i = 1,2,3
    list.append(i)

print(list)

# 3
tuple1 = (5,6)
list.append(tuple1)

print(list)

# 4
languages = ["Java", "Python", "php"]
list.append(languages)

print(list)

# o/p:
# [1, 2, 3]
# [1, 2, 3, 1, 2, 3]
# [1, 2, 3, 1, 2, 3, (5, 6)]
# [1, 2, 3, 1, 2, 3, (5, 6), ['Java', 'Python', 'php']]