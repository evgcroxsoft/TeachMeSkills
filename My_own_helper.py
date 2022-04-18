string = 'Zhenya'
integer = 25
boolean = False
dictionary = {'name' : 'Dmitriy', 'gender' : 'M'}
set = {1,2,3,2,2,1,1,2,2,}
float = 1.25
tuple = ('Sunday','Monday','Tuesday','Wednesday')
tuple_2 = ({'name': 'Fedor', 'surname': 'Ivanov', 'gender': 'M'})
list = [string,integer,boolean, dictionary, set,float,tuple]

string, integer, boolean = 'Zhenya', 25, False 
''' Можно писать переменные в одну строку'''

for key in tuple_2:
    print (key,':',tuple_2[key])
for value in tuple_2.items():
    print(value)


a = dictionary['name']
b = list[0]
c = list[3]['gender']
d = tuple[0]
print(a)
print(b)
print(c)
print(d)
abc = list.append('Hello World')
print(list)

# Перебираем значения в коллекции для аргумента "i". 
for i in list:
    if i == 1.25:
        print('We Found')

for i in range(1,10):
    print(i)

e = [i*2 for i in range(1,10)]
print(d)

f = [(tuple[0],tuple[3]) for i in range(5)]
print(f)

print(f'My name is {a}')

dictionary = {'name' : 'Dmitriy', 'gender' : 'M'}
a = dictionary['name']
print(f"My name is {dictionary['name']}")


z = list.count(1.25)
print(z)


s = [1,2,4]
k = iter(s)
print(next(k))
print(next(k))
print(next(k))

# Regex - ищем в тексте что нам нужно
import re
target_string = "My name is Evgeniy I am 36"
world_list = re.split(r"\s+",target_string)
print(world_list)

regex = r"([a-zA-Z]+) (\d+)"

match = re.search(regex,"I was born on June 24")
if match != None:
    print(f"Match at index: {match.start()},{match.end()}")
    print("Full Match: %s" % (match.group(0)))
    print(f"Month: {match.group(1)}")
    print("Day: %s" % (match.group(2)))

#Regex 2 - меняем в тексте что нам нужно

pattern = '\s+'
replace = ''
string = 'Z h e n y a'
new_string = re.sub(pattern,replace,string)
print(new_string)

# Regex 3 - проверка емейла
value = input('Enter you email: ')
pattern = r"^[a-zA-Z0-9!s%&'*+\-\/=?^_`{|}~]+@[a-zA-Z0-9_]+\.{1}[a-zA-Z0-9_]{,63}$" 
print(f'Lenght:{len(value)}')
if re.fullmatch(pattern,value):
    print ('Match')
else:
    print('No Match')