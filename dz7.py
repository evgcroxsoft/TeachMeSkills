with open('user.txt', 'r') as test:
    for i in test:
        print(i[1:10])

 import json
 data = json.load('users.json')
 print(data)
