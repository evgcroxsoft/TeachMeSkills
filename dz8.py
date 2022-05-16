# 1. сделать класс. 2. Сделать класс наследник 3. Переопределить метод родителя  4. *Перегрузить метод __init__

class Child:
    def __init__(self, name: str, surname: str, born):
        self.name = name,
        self.surname = surname,
        self.born = born
    
    def lenght (self):
        return len(str(self.name))


class Parent(Child):
    def __init__(self, education, married_status, **kwargs):
        self.education = education,
        self.maried_status = married_status,
        super().__init__(**kwargs)

    def lenght (self):
        return (f'Переопределили метод родителя: {len(str(self.surname))}')
    
    def __str__(self):
        return f'This is my new name {self.name}'
        

alex = Child(
    name = 'Alexey',
    surname = 'Redko',
    born = '25-05-1985'
    )


adult = Parent(
   name ='Mikle',
   surname = 'Jordan',
   born = '02-02-2000',
   education ='magistr',
   married_status= 'married',
   )


print(alex.name, alex.surname, alex.born, alex.lenght())
print(f"{alex.name}, {adult.name},'He has education: {adult.education}", adult.lenght())
print(Parent.mro())
print(str(adult))