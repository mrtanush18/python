users_data={1: {"general": {"age": 45,"name": "John"},"car_data": {"general": {"type": "mercedes","model": "GLE"}},"additional": {"first_commit": {"list_of_attempts": [{"type": "main"}]}}}}

# print(users_data[1]["additional"]["first_commit"]["list_of_attempts"][0]["type"])

for key,value in users_data.items():
    for k2,v2 in value.items():
        for k3,v3 in v2.items():
            temp = type(v3)      # or isInstance()
            if temp == dict:
                for k4,v4 in v3.items():
                    if type(v4) == list:
                        print(v4[0]['type'])
                    # temp2 = type(v4)
                    # if temp2 == list :
                    #     for element in v4:
                    #         for k5,v5 in element.items():
                    #             print(v5)
                                                





            # for v3 in v3.items():
            #     print(v3)





# users_data={
#   1: {
#     "general": {
#       "age": 45,
#       "name": "John"
#     },
#     "car_data": {
#       "general": {
#         "type": "mercedes",
#         "model": "GLE"
#       }
#     },
#     "additional": {
#       "first_commit": {
#         "list_of_attempts": [
#           {
#             "type": "main"
#           }
#         ]
#       }
#     }
#   }
# }