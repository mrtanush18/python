dict = {'a': 100 , 'b': 200 , 'c': 400}

sum = 0

for j in dict:
    sum = sum + dict[j]

print(sum) 
# o/p : 700

key = ""

for k in dict:
    key = key + str(k)  # concat string 

print(key)  
# o/p : abc
