# Find max element from sub lists without using max method in list comprehension
# FUNCTIONS 1

list = [[1,2,3],[4,5,6],[7,8,9]]

sub_list_max = []

def getMaxSubElement(sub_list):
    # sub_list_max.append(max(sub_list))
   max = 0
   length = len(sub_list)
   for j in sub_list:    # used only 1 loop as already we have inner lists in sub_list
        if max < j:
            max = j
   sub_list_max.append(max)


list_compre = [getMaxSubElement(sub_list) for sub_list in list]

print(sub_list_max)
