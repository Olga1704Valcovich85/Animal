#Построить три класса (базовый и 3 потомка), описывающих некоторых хищных животных (один из потомков),
# всеядных(второй потомок) и травоядных (третий потомок).
# Описать в базовом классе абстрактный метод для расчета количества и типа пищи,
# необходимого для пропитания животного в зоопарке.
from abc import ABC, abstractmethod
class Animal(ABC):
    def __init__(self, name="none", tip = 'none', massa = 0):
        self.name = name
        self.tip = tip
        self.massa = massa

    @abstractmethod
    def eat(self, ):
        pass
    @abstractmethod
    def tip_eat(self):
        pass


class Hisch(Animal):
    def eat(self, ):
        if self.tip == 'хищник':
            print("Животное питается мясом")
        elif self.tip =="всеядный":
            print('Животное можно кормить мясом и овощами')
        else:
            print('Животное питается травой и овощами')
    def tip_eat(self):
        m = []
        if self.tip == 'хищник':
            s = self.massa*0.35
            m.append(s)
            print('Количество еды', m,  "разделить на два приема")
        elif self.tip =="всеядный":
            s = self.massa * 0.35
            m.append(s)
            print('Количество еды', m, "разделить на два приема")
        else:
            s = self.massa * 0.35
            m.append(s)
            print('Количество еды', m, "разделить на два приема")

class Obsch(Animal):
    def eat(self, ):
        if self.tip == 'хищник':
            print("Животное питается мясом")
        elif self.tip == "всеядный":
            print('Животное можно кормить мясом и овощами')
        else:
            print('Животное питается травой и овощами')
    def tip_eat(self):
        m = []
        if self.tip == 'хищник':
            s = self.massa*0.35
            m.append(s)
            print('Количество еды',  m, "разделить на два приема")
        elif self.tip =="всеядный":
            s = self.massa * 0.35
            m.append(s)
            print('Количество еды', m, "разделить на два приема")
        else:
            s = self.massa * 0.35
            m.append(s)
            print('Количество еды', m, "разделить на два приема")
class Trav(Animal):
    def eat(self, ):
        if self.tip == 'Хищник':
            print("Животное питается мясом")
        elif self.tip == "Всеядный":
            print('Животное можно кормить мясом и овощами')
        else:
            print('Животное питается травой и овощами')
    def tip_eat(self):
        m = []
        if self.tip == 'Хищник':
            s = self.massa*0.35
            m.append(s)
            print('Количество еды', m, "разделить на два приема")
        elif self.tip =="Всеядный":
            s = self.massa * 0.35
            m.append(s)
            print('Количество еды', m,  "разделить на два приема")
        else:
            s = self.massa * 0.35
            m.append(s)
            print('Количество еды', m, "разделить на два приема")

tigr = Hisch('Tигр', 'хищник', 50)
tigr.eat()
tigr.tip_eat()