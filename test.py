# from datetime import datetime


# def decorator(func):
    
#     def wrapper(val):
#         start = datetime.now()
#         func(val)
#         end = datetime.now()
#         tim = end-start
#         return tim
#     return wrapper


# @decorator
# def reverse(val):
#     reversed =''
#     for i in range(1, (len(val)+1)):
#             reversed += val[len(val)- i]
#     return reversed


# c = reverse('Zhenya')
# print(c)


# print('ABC CaBA'[7:1:-1])


# # print('astihculop osv aybet u yexelA'[::-1])





# # var = 'James Bond'
# # print(var[2:1:-1])






# class Employee:  
#     def __init__(self, name, salary):  
#         self.name = name  
#         self.salary = salary  

#     def game(self,a,b):
#         return a + b


# print(Employee('Fedor', 'Taras').name)
# print(Employee('Fedor', 'Taras').game(5,5))
# print(Employee(3,3).game(5,5))



# def foo(a,b):
#     c = a + b
#     return c

# foo(1,5)

# print(foo(1,5))




# from datetime import datetime

# def decorator(func):
    
#     def wrapper(val):
#         start = datetime.now()
#         func(val)
#         end = datetime.now()
#         tim = end-start
#         return tim
#     return wrapper

# @decorator
# def reverse(val):
#     reversed =''
#     for i in range(1, (len(val)+1)):
#             reversed += val[len(val)- i]
#     return reversed

# c = reverse('TeachMeSkills')
# print(c)



# for i in range(100):
#     i = i + 1
#     print(i)
# else:
#     print('Finish')

# from datetime import date, timedelta

# start = date(2022,10, 1)
# end = date(2022,10, 5)
# date = date(2022,10, 3)

# if start <= date <= end:
#     print("in between")
# else:
#     print("No!")



import datetime

def check_dates(booking_date_start, booking_date_end, searching_date_start, searching_date_end):
    
    d1 = datetime.date.fromisoformat('2022-10-01')
    d2 = datetime.date.fromisoformat('2022-10-25')
    d3 = datetime.date.fromisoformat('2022-10-10')
    d4 = datetime.date.fromisoformat('2022-11-15')
    d1 = booking_date_start
    d2 = booking_date_end
    d3 = searching_date_start
    d4 = searching_date_end
    days = [d1 + datetime.timedelta(days=x) for x in range((d2-d1).days + 1)]
    days2 = [d3 + datetime.timedelta(days=x) for x in range((d4-d3).days + 1)]
    for day in days:
        for i in days2:
            if day == i:
                return True
    return False


d1 = datetime.date.fromisoformat('2022-10-01')
d2 = datetime.date.fromisoformat('2022-10-25')
d3 = datetime.date.fromisoformat('2022-10-10')
d4 = datetime.date.fromisoformat('2022-11-20')
print(check_dates(d1, d2, d3, d4))

