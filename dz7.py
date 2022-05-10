# with open('users.json', 'r') as test:
#     for i in test:
#         print(i[1:10])



import json
with open('users.json') as users_file:
    data = json.loads(users_file.read())
    for i in data:
        new_list = []
        list.append(i)
        print(type(i))
