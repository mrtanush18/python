dict = {1:'one', 2:'two', 3:'three'}
dict2 = {4:'four', 5:'five', 6:'six'}

print(dict)
# o/p:
# {1: 'one', 2: 'two', 3: 'three'}

for keys,values in dict2.items():
    dict.update(dict2)
    
print(dict)
# o/p:
# {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six'}

# 5 Ways to merge dictionaries
# https://towardsdatascience.com/merge-dictionaries-in-python-d4e9ce137374