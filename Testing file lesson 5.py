# def add (a,b):
#     return a+b

# add(1,11)

# print(add)


#Система должна мне сказать естли в слове больше буквы

# name_1 = 'Zhenya'
# name_2 = 'Katya'
# name_3 = 'Kedor'

# for upper in name_1:
#     if upper.isupper() == True:
#         print('UP1')


# for upper in name_2:
#     if upper.isupper() == True:
#         print('UP2')

# for upper in name_3:
#     if upper.isupper() == True:
#         print('UP3')


# a = 'Privet vsem'
# def check_if_containers_upper (string):
#     is_containers_upper = False
#     for let in 'String':
#         print(let)
#         if let.isupper():
#             print(f'ISUPPER: {let}')
#             is_containers_upper = True
#             break
#     return(is_containers_upper)
# print(check_if_containers_upper(a))










# Write function which can give us True if the String has a Upper lit

# def if_string_upper (string):
#     string = input('Enter: ')
#     for litera in string:
#         if litera.isupper():
#             return True
#     return False
        
     
        

# print(if_string_upper(if_string_upper))




# def func_name(name)->bool:
#     '''
#     This function about Upper case
#     '''
#     name = input('Enter your name please: ')
#     for bukva in name:
#         if bukva.isupper():
#             print('Hello')
#             return True
#     return False
            
# print(func_name(func_name))



# a = 10
# def numbers():
#     global x 
#     x = 20

# numbers()
# print(a)


# '''
#  We write about how it works under hood.
# '''
# numbers = [5,5]
# for i in range(15):
#     numbers.append(i)
# print(numbers)



# numbers = [i for i in range (15)]
# print(numbers)


# Написать функцию, которая принимает в себя список и возвращает в список, состоящий только из четных элементов

# def parnie (a):
#     a = int(chisla)
#     for i in range(chisla):
#         print(chisla)
#         if i %2 == 0:
#             print (chisla)


# parnie()

# def chetniy():
#     list = []
#     a = int(input('Print:',))
#     for i in range(a):
#         if i %2 == 0:
#             list.append(i)
#     print(list)

# chetniy()



# def chetniy(a = int(input('Enter your digit:',))):
#     list = []
#     for i in range(a):
#         if i %2 == 0:
#             list.append(i)
#     print(list)

# chetniy()

# lists = [0,1,3,4,5,6,7,8,9]
# def chetniy(lists):
#     new_list = [i for i in lists if i % 2 ==0]
#     return(new_list)

# print(chetniy(lists))


# Написать функцию, котора будет принимать в себя список людей, и будет возращать список мужчин и список женщин

person = [
    {'name':'Dmitriy','gender':'M'},
    {'name':'Hanna','gender':'W'},
    {'name':'Julia','gender':'W'},
    {'name':'Evgeniy','gender':'M'},
    {'name':'Hleb','gender':'M'},
    {'name':'Konstantin','gender':'M'},
    {'name':'Anastasia','gender':'W'},
    
]

def guest_list():
    gen = [d['gender'] for d in person]
    men = [d['name'] for d in person if d['gender'] == 'M']
    women = [d['name'] for d in person if d['gender'] == 'W']
    d,f=0,0
    for i in gen:
        if i == 'M':
            d+=1
        elif i == 'W':
            f+=1
    return(f'Total = {d+f},\nMan = {d}:{men},\nWoman = {f}{women}')

print(guest_list())


# result = next(d['Age'] for d in example['list'] if d.get('Surname') == 'surname5')
# # result = next(d['Age'] for d in example['list'] if d.get('Surname') == 'surname5')


# dict = [{'name':'Zhenya','gender':'M'},{'name':'Katya','gender':'W'}]

# for i in dict[0]['gender']:
#     print(i)




# def gender(person):

#     print[i for i in my_dict['index'] for k in i]
#         print('Man')









# def chetniy():
#     list = [i for i in range(a)]
#     a = int(input('Print:',))
#     if list %2 == 0:
#         list.append(list)

# chetniy()

# def numbers(list):
#     num = ()
#     for num in list:
#         if num %2 == num:
#             print(num)






