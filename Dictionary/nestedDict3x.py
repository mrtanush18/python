# Take user input for a 3 level nested dictionary and print emp1 and 2 details
# MOST IMP LINE : dict[outer_key] = value (TO AVOID OVERWRITING OF VALUES)

dict = {}

for i in range(2):
    outer_key = input('\nEnter outer key ')  
    value = {}

    for j in range(1):  
        key1 = input('\nEnter inner key ')  
        value1 = {}
        value[key1] = value1              

        dict[outer_key] = value            

        for k in range(2):
            key2 = input('\nEnter innermost key ')  
            value2 = input('Enter innermost value ')

            value1[key2] = value2

print("\n",dict)
# o/p :
# {'emp1': {'mob': {'phone1': '981', 'phone2': '982'}}, 'emp2': {'mob': {'phone1': '983', 'phone2': '984'}}}

for key in dict:                           # used .items on all loops to access innermost keys,values
    print("\nEmp_id:",key)

    for key1 in value.items():
        print(key1)

        for key2,value2 in value1.items():
            print(key2,":",value2)

# dict['emp2']['mobile']['phone2']

# o/p :
# Emp_id: emp1
# mob
# phone1 : 981
# phone2 : 982

# Emp_id: emp2
# mob
# phone1 : 983
# phone2 : 984

