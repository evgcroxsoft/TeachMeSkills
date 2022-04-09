# 1. Python3 was downloaded successfully

# 2. Написать программу, которая будет выводить приветствие с Вашим именем;
name = ('Hi, Evgeniy!')
print(name ,'\n')

# 3. Написать программу, которая посчитает и выведет результат выражения:
# ((2**5)*2 - 16 * 2)/(8**8)
expression = ((2**5)*2-16*2)/(8**8)
print('Result of expression:((2**5)*2 - 16 * 2)/(8**8) is', expression, '\n')

# 4. Проверить является ли результат выражения выше типом данных Int
print('Is data type of expression Integer?:',type(expression) is int,'\n')

# 5. Создать и вывести список, хранящий в себе все рассмотренные в данной лекции типы данных
data_type_none = a = None
data_type_string = b = 'Zhenya'
data_type_dictionary = c = {'father':'Peter', 'mother':'Katryn', 'email':'per@gmail.com' }
data_type_integer = d = 5
data_type_float = e = 1.333
data_type_set = f = {1,2,1,1,6,6,4,2,3,8,8,89,9,9,9,}
data_type_tuple = g = ('Sunday', 'Monday', 'Tuesday', 'Thirsday', 'Friday', 'Saturday')
data_type_list = total = [a,b,c,d,e,f,g]
print('Data_type_List: None, String, Dictionary, Integer, Float, Set, Tuple: ', total,'\n')

# 6. Дополнительно для закрепления материала:
    #a - изменим в List email на pupkin@gmail.com
total[2]['email'] = ('pupkin@gmail.com')
print(total,'\n')
    #b - перевести Float в Integer
digit = int(e)
print(type(digit),(digit))
