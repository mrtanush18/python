list2 = [1,4,4,7,7,9]
new_list = []

for i in list2:            
    if(i not in new_list):
        new_list.append(i)

print(new_list)
# [1, 4, 7, 9]

# _________________________________________________________________________________
# # Wrong:
# list2 = [1,4,4,7,7,9]
# new_list = []
# length = len(list)

# for i in range(length):
#     if(list2[i] != list2[i+1]):
#         new_list.append(list2[i])
#     else:
#         continue

# print(list)