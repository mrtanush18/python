# Dynamic Nested dictionary : {emp1:{name: , job:}}

dict = {}
size = int(input("size "))

for i in range(size):
    outer_key = input('\nOuter key ')

    value = {}  # Create new dict

    for j in range(2):  # Input values in new dict
        key = input('\nEnter key ')
        val = input('Enter value ')
    
        value[key] = val
        dict[outer_key] = value

print(dict)
# o/p :
# {'emp1': {'name': 'tanush', 'mob': '981'}, 'emp2': {'name': 'rachit', 'mob': '982'}}




# ______________________________________________________________________________________
# >>> To create a nested dictionary with fixed no. of inner keys & values

# Create a nested dictionary taking user input
# Ex.dict = {1:{'sam':'983359652'}, 2: {henry:xxx}, 3: {john: yyy} }

# dict = {}
# size = int(input("Enter size"))
# value = {}

# for i in range(size):
#     key = input("Enter outer key")
#     inner_key = input("Enter inner key")
#     inner_value = input("Enter inner value")
#     value.update({inner_key : inner_value})
#     dict.update({key:value})

# print(dict)