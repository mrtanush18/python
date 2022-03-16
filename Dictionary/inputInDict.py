# Take key,value from user and create dictionary and print it

dict = {}
size = int(input("\nEnter number of items: "))

for i in range(size):
    key , value = input("\nEnter key and value: ").split()
    dict[key] = value

print('\n',dict)
# o/p :
# {'name': 'tanush', 'age': '22'}

dict["6"] = "ruby"
dict.update({"6":".NET"})
print('\n',dict)

# o/p:
# {'name': 'tanush', 'age': '22', '6': '.NET'}
