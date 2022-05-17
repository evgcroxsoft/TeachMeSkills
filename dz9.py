# 1. Сделать свой класс данных 
# 2. Добавить в класс статик метод, 
# 3. Добавить в класс классметод, 
# 4. cписок хрянящий в себе 5 объектов датакласов,
# 5. *Создать метакласс
# 6. Регистрацию сделать через ООП

class Player:

    TOTAL_PLAYERS = 0

    def __init__(self, name, surname, country, mood):
        self.name = name
        self.surname = surname
        self.country = country
        self.mood = mood
        Player.TOTAL_PLAYERS = Player.TOTAL_PLAYERS + 1

    @property
    def name_surname(self):
        return f'{self.name} {self.surname}'


# 2. Добавить в класс статик метод, 
    @staticmethod
    def compare(player_1,player_2):
        print(f'Player1 lenght:',len(str(player_1.name)))
        print(f'Player2 lenght:',len(str(player_2.name)))
        a = len(str(player_1.name))
        b = len(str(player_2.name))
        if a > b:
            return True
        else: 
            return False

    @staticmethod
    def say_hello(self):
        print (f'Say_hello {self.name}')

# 3. Добавить в класс классметод:
    @classmethod
    def total_players(cls):
        print('@classmethod: Total players: ', cls.TOTAL_PLAYERS)

player_1 = Player(
    name= 'Djoy',
    surname = 'Polix',
    country = 'USA',
    mood ='Ok'
    )

player_2 = Player(
    name= 'Boris',
    surname = 'Puty',
    country = 'California',
    mood = 'Ok'
    )

print('@property: ',player_1.name_surname) #@property
print('@staticmethod:', Player.compare(player_1,player_2))#@staticmethod
print('@staticmethod:',Player.say_hello(player_1))#@staticmethod
Player.total_players()#@classmethod

# 4. Cписок хрянящий в себе 5 объектов датакласов:

from dataclasses import dataclass

@dataclass
class Human:
    sex: str
    age: int

human_1 = 'Woman',33
human_2 = 'Woman',25
human_3 = 'Man',17
human_4 = 'Man',60
human_5 = 'Woman',42

list = [human_1,human_2,human_3,human_4, human_5]

print('@Dataclass:', list)

# 5. *Создать метакласс

team = type("Team",(Human,Player),{'team_name':'Teachmeskills', 'method':lambda self: self.team_name})
print ('@Metaclass:',team('Woman',50))
