# Reverse list using n/2 iterations

list = [100,-56,5,6,7,8]
count = 0
j = -1

print('OG list: ',list)

# HOW TO SWAP LIST ELEMENTS

for i in range(len(list)//2):  # // : floor div operator to round to nearest whole no.
        temp = list[i] 
        list[i] = list[j]
        list[j] = temp
        j = j - 1
        count = count + 1
        
print("\nReversed list:",list)
print('\nNo. of iterations: ', count)

# o/p:
# OG list:  [100, -56, 5, 6, 7, 8]
#  Reversed list: [8, 7, 6, 5, -56, 100]
# No. of iterations: 3

# TRACING:

# range : 3

# i = 0  
# j = -1
# temp = 100
# list[0] = 8
# list[-1] = 100

# [8,-56,5,6,7,100]

# i = 1
# j = -2
# temp = -56
# list[1] = 7
# list[-2] = -56

# [8,7,5,6,-56,100]

# i = 3
# j = -3
# temp = 5
# list[2] = 6   
# list[-3] = 5

# [8,7,6,5,-56,100]