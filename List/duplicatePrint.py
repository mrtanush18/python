# Print item in list is ocurring x times if duplicate

list = [5,10,10,12,12,28,10]

count = {}  # dictionary

# HOW TO INCREMENT VALUE IN DICTIONARY

for j in list:
    if j not in count:
        count[j] = 1                    # 12 : 1
    else:
        count[j] = count[j] + 1         # # 12 : 1 + 1

print(count)

# HOW TO PRINT KEY & VALUE FROM A DICTIONARY IN A SPECIFIED FORMAT

for k,v in count.items():
    if(v>1):
        print(k, "is duplicate & occurs", v ,"times")  

# Old version :
# for k in count:
#     if(count[k]>1):
#         print(k, "is duplicate, occurring", count[k] ,"times")   # k is key, count[k] is value

# o/p:
# {5: 1, 10: 3, 12: 2, 28: 1}
# 10 is duplicate, occurring 3 times
# 12 is duplicate, occurring 2 times

# Tracing :
# 5 not there in new so goes in else statement and 5 : 1
# Same for 10
# Next again 10 so goes in if statement & 10 : 1 + 1 --> 10 : 2