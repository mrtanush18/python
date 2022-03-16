#  Find number of unique elements ex. list = [1,2,2,4,6,4,9]
# count = 5

list = [1,2,2,4,6,4,9,1]  # 1,2,4,6,9

new = []

for i in list:
    if i not in new:
        new.append(i)

print("There are",len(new),"unique elements in given list")

# o/p:
# There are 5 unique elements in given list

# NOT POSSIBLE WITHOUT USING SECOND LIST :

# num = list[0]
# count = 0

# for i in range(1,len(list),1):
#     if list[i] != num:
#         count = count + 1
#         num = list[i]
#     else:
#         num = list[i]

# print("There are",count,"unique elements in given list")

