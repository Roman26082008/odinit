""" что такое лямбда и как работает
f = lambda a, b: a + b
a = 5
b = 4
print(f(a, b))
"""


"""из функций для каких либо аргументов извлечь принимающюю фунцию для двух аргументов
from functools import reduce
numbers = [2, 1, 3, 4, 5]
product = reduce(lambda x, y: x + y, numbers, 1)# значение 1 это с чего начинается numbers
print(product)
"""


""" один в один функция только с def
def avg(num):
    pr = 1
    for n in num:
        pr *= n
        return pr


num = [2, 3, 4, 5, 6, 7]
pr = avg(num)
"""


""" функция map, plus которая складывает список лист 
def plus(a, b, c):
    return a + b + c
x = map(plus, [1, 2], [3, 4], [5, 6])
print(list(x))
"""


"""#zip - фунция обьединяющая два или более списка(1, sugar и т.д)
for i in zip([1, 2, 3], ['sugar', 'spice', 'everything nice']):
    print(i)
    
FIRST EXAMPLE
x = [5, 6, 7]
y = [4, 3, 4]
v = zip(x, y)
c = list(v)
print(c) 

SECOND EXAMPLE
lst1 = [1, 2, 3, 4]
lst2 = [5, 6, 7, 8]
lst3 = ['one', 'two', 'three', 'four']
for a, b, c in zip(lst1, lst2, lst3):
    print(f'{c}:\t{a}+{b}={a+b}')
"""



""" filter- фильтрует список по указанному класcу
num = [1, 2.0, 3.1, 4, 5, 6]
f = filter(lambda x: type(x) is int, num)
print(list(f))

FIRST EXAMPLE
num = [4, 5, 6, 7, 8]
f = filter(lambda x: x > 4, num)
print(list(f))

SECOND EXAMPLE
num = [False, 1, 3, 4]
print(list(filter(None, num)))
"""




""" так же можно работать с листами (max, min, sorted)
a = {'a': 10, 'b': 15, 'c': 4}
list_d = list(a.items())
list_d.sort(key=lambda i: i[1])
print(*list_d)


SECOND EXAMPLE IS DICT
a = [-10, 3, 4, 7]
doit = {'abs': lambda x: x - 1, 'spb': lambda x: (x) - 1, 'zrd': lambda x: x}
for i in a:
    if i > 0 :
        print(doit['abs'](i))
    elif i < 0:
        print(doit['spb'](i))
    else:
        print(doit['zrd'](i))
"""


""" talk с помощью которого можно изменять функцию
def hello(name):
    return f'Привет {name}.'
print(talk(hello))
"""


"""
18.12.23 ЗАДАЧА ОДИН
"""
""" задача лямбду и reduce нужно умножить весь список друг на друга
from functools import reduce
numbers = [1, 2, 3, 4, 5]
list_1 = reduce(lambda x, y: x * y, numbers)
print(list_1)
"""



""" ПРОИЗВЕДЕНИЕ С ПОМОЩЬЮ БИБИЛИОТЕКИ MATH.PROD(ОТВЕЧАЕТ ЗА СЛОЖЕНИЕ ПЕРЕМЕННЫХ)
import math
a = list(map(int, input("Введите число").split(" ")))
print(math.prod(a))
"""


""" ПРОИЗВЕДЕНИЕ С ПОМОЩЬЮ ПОЛЬЗОВАТЕЛЬСКОЙ ФУНКЦИИ
def avg(x):
    avg = 1
    for i in x:
        avg *= i
    return avg
a = list(map(int, input("введите число")))
print(avg(a))
"""


""" ЗАДАЧА НА ВЫВОД СЛОВ В КОТОРЫХ 5 БУКВ

     FIRST EXAMPLE
words = input("введите слова").split(" ")
print(*sorted(list(filter(lambda x: len(x) == 5, words))))

SECOND EXAMPLE
words = input("введите слова").split(" ")
print(*sorted([i for i in words if len(i) == 5]))
"""



"""
def task (a, b):
    print(f'Первое число {a}')
    print(f'Второе число {b}')
    try:    #это процесс который должен выполняться верно
        print(f'результат {float(a+b)}')
    except TypeError:   #для исключений как elif (здесь мы можем написать ошибку которая у нас будет)#так же except можно делать для разных видов ошибок сразу
        print(f'результат', str(a)+str(b))
    except ZeroDivisionError:
        print(f'Вы не можете разделить на 0')
    except:
        print('Что то пошло не так')
    else:
        print('Все хорошо вы вывели числа')
    finally:
        print('конец')
task(5, 4) #это результат в исключении
task(5, 'roma')
"""
"""
import time   #библиотека таймера


def decorator(funk):
    def snopy(*args, **kwargs):
        start = time.time()   #выводим время
        funk(*args, **kwargs)       #это декоратор по умолчанию
        end = time.time()
        print('Функция выполнилась', round(end - start, 2))  #округляет до 2
    return snopy
@decorator   #мы это написали для того , чтобы result отнести к decorator
def result(a):   #функция для вызова результата
    time.sleep(9) #задержка может быть любой ,для того чтобы декоратор успел подсчитать
    print(a*a)
result(0.5050)
"""





""" ЗАДАЧА НА ПОСТРОЕНИЕ ЧИСЕЛ В НУЖНОМ ПОРЯДКЕ ПРАК.3
a = [1, 2, -3, -5,  5]
print(*sorted(list(filter(lambda x:x[-2:] , a))))
"""









""" 10 января - использование dir .Когда мы его использовали можем обращаться к другим атрибутам
class Phone:
    pass

print(dir(Phone))
"""








""" это статические поля -находятся внутри класса ,но не в функциях
class Phone:

    model = 'Vesta'
    color = 'White'

def vesta():
    pass
                  #Для каждого значение создаем функцию
def svet():
    pass

print(Phone.model)
Phone.color = 'Black'   #так же мы можем изменять переменные и выводить их
print(Phone.color)
"""




"""
#динамические поля - внутри функции
class Phone:
#статические поля
    model1 = '12324'
    color1 = 'white'
def __init__(self, color, model):
#динамические поля - которые находятся внутри функции
    self.color = color
    self.model = model

print(Phone.color1)
print(Phone.model1)
"""




""" Это статический метод выполнения функции
class Phone:

    @staticmethod
    def model(mode):
        if mode == '734':
            return 'Это та модель'
        elif mode == '345':
            return 'Это apple'
        else:
            return None

    def model_finish(self, model):
        pass

print(Phone.model('345'))
"""




""" Это класс метод
class Phone:
    @classmethod
    def avg(cls, color):
        Phone = cls(color, 'Toy', None)
        return Phone
        """





"""
# это пример решения через OOP
class Cat:
    def __init__(self, color, age, breed):
        self.color = color
        self.age = age
        self.breed = breed

    def meow(self):
        print('мяу')

    def mur(self):
        print("мур")


cat1 = Cat('рыжая', 4, 'разводим')
cat2 = Cat('черная', 6, 'не разводим')

cat1.meow()
cat2.mur()
"""





"""#ПРАКТИКА 10.02.2024 ЗАДАЧА НА ДЕЙСТВИЯ С ДОЛЛАРАМИ С ПОМОЩЬЮ МЕТОДОВ И КЛАССОВ
class Many:
    #можно не указывать , играют роль по умолчанию
    r = 0
    k = 0

    def __init__(self, r, k):
        self.r = r
        self.k = k

    def intotal(self):
        print('$', int(self.r), ',', int(self.k), sep='')

    def addition(self, r, k):
        self.r += r
        self.k += k
        self.r += self.k // 100 #тоесть если 100 копеек , то +1 рубль
        self.k %= 100 #делаем проверку, если количество копеек превышает 100,  остаток записывается к рублям
        print('+$', r, ',', k, sep="")

    def subtraction(self, r, k):
        self.r -= r
        self.k -= k
        self.r -= self.k // 100
        self.k %= 100
        print('-$', r, ',', k, sep="")


    def division(self, number):
        self.r /= number
        self.k /= number
        self.r //= 1 #чтобы при делении рублей само на себя выводилось 1
        self.k += (self.r % 1) * 100 // 1 # действие благодаря которому все делится
        print('/', number)


    def mult(self, number):
        self.r *= number
        self.k *= number
        self.r += self.k // 100  # тоесть если 100 копеек , то +1 рубль
        self.k %= 100
        print("*", number)


    def comparison(self, num_rub, num_cop):
        if num_rub > self.r:
            print(f'{num_rub}, {num_cop} >')
        elif num_rub < self.r:
            print(f'{num_rub}, {num_cop} <')
        elif num_cop > self.k:
            print(f'{num_rub}, {num_cop} >')
        elif num_cop < self.k:
            print(f'{num_rub}, {num_cop} <')
        else:
            print(f'{num_rub}, {num_cop} =')



money = Many(12, 45)
money.intotal()
money.addition(13, 75)
money.intotal()
money.subtraction(13, 75)
money.intotal()
money.division(3)
money.intotal()
money.mult(3)
money.intotal()
money.comparison(12, 44)
"""










#ПРАКТИКА 12 ЯНВАРЯ АТТЕСТАЦИОННЫЕ МОМЕНТЫ
"""
#РАЗБОР СИТУАЦИИ К ОБРАЩЕНИЮ 
class Test:
    a = 'hello'
test = Test()      # ЭТО ЭКЗЕМПЛЯР КЛАССА
print(test.a)
setattr(test, 'value', 9) #это дополнение test = экземпляр , value- название , 5 - это значение
print(test.value) #обращаемся к названию и выводится в данном случае 9
"""



"""
#ПЕРЕМЕННЫЕ КЛАССЫ
class Shark:
    animal_tupe = "fish" #'это переменные в классе
    loca = "ocean"
    followers = '5'

new_shark = Shark() # присваиваем экземпляр Shark
print(new_shark.animal_tupe) #выводим значение
print(new_shark.loca)
print(new_shark.followers)
"""




"""
#ПРИМЕРЫ ПЕРЕМЕННЫЕ ЭКЗЕМПЛЯРА КЛАССА (SELF.NAME)
class shark:
    #переменные класса
    animal_type = 'fish'
    loca = 'ocean'


    #метод конструктор с переменными экземпляра name и age
    def __init__(self, age, color, animal):
        self.age = age
        self.color = color# ЭТО ВСЕ ПЕРЕМЕННЫЕ ЭКЗЕМПЛЯРА КЛАССА
        self.animal = animal

#метод переменной экземпляра followers
    def follower(self, followers):
        print("У этой рыбки"+str(followers)+"подписчиков")

#обьект.установка переменных экземпляра метода-конструктора
new_shark = shark(2, 'blue', 'parrot')
#выводим метод follower
new_shark.follower(15)
print(new_shark.age)
print(new_shark.color)
print(new_shark.animal)
print(new_shark.animal_type)
print(new_shark.loca)
print()
"""



"""
#задача на вывод данных анкеты 
class alfavit:

    def __init__(self, age, gender, name):
        self.age = age
        self.gender = gender
        self.name = name

    def write_anketa(self):
        return str("Его имя>>>>>>"+str(self.name)+"\tЕго возраст>>>>"+str(self.age)+"\tЕго гендер>>>>>"+str(self.gender))
rnm = alfavit(10, "я бисексуал", "тюлень")
print(rnm.write_anketa())
"""


"""
#1 ЗАДАЧА описание классовой структуры
class alfavit:
    def __init__(self, yazik, spicok):
        self.yazik = yazik
        self.spicok = spicok

    def write(self):
        print("список всех букв", self.spicok)

    def va(self):
        return "кол-во букв", len(self.spicok)

an = alfavit("russian", "абвгдеежзийклмнопрстуфхцчшщьыьэюя")
an.write()
print(an.va())
"""





"""
# задача путем унаследования к дочерним классам c помощью статических элементов
import string #хранит в себе ряд библиотек с алфавитами , цифрами и знаками
class Alfavit:
    def __init__(self, language, leters_str):
        self.language = language #английский язык
        self.leters = list(leters_str)



#выводим буквы алфавита
    def print(self):
        print(self.leters)

# выводим количество алфавита
    def letters_num(self):
        return len(self.leters)

class EngAlfavit(Alfavit): #создаем дочерний класс

    __letters_num = 27 #создаем статическое поле со значением

    def __init__(self):
        super().__init__('Eg', string.ascii_uppercase)#super() мы передаем этому классу значения

    def is_in_letters(self, leters):
        if leters.upper() in self.leters: #проверяем большие английские буквы с предыдущего класса и возвращаем их
            return True
        return False


    def letters_num(self):
        return EngAlfavit.__letters_num #выводим количество букв #так же мы могли вывести конечный итог без принта ,указав вместо return здесь

    @staticmethod #сохдаем статический метод по заданию
    def example():
        print("qwerty")

#мы создали обьект класса EngAlfavit()
obg = EngAlfavit()
obg.print() #мы вывели весь алфавит которые задали в классе alfavit через библиотеку
print(obg.letters_num()) #вывели колличество букв
print(obg.is_in_letters('F'))#элементы для проверки
print(obg.is_in_letters('a'))#элементы для проверки
EngAlfavit.example()
"""


"""

#НЕЗАКОНЧЕННАЯ ЗАДАЧА
class Human:              #информация о человеке
    defolt_name = "nonaem"     #начальное положение ноунейм
    defolt_age = 0          #начальный возраст 0
    def __init__(self, name = defolt_name, age = defolt_age):         #мы создали значение по умолчанию
        self.name = name
        self.age = age       #все здесь выводим
        self.__money = 0        #отмечаем что у него ноль денег (и мы создали приват параметр)
        self.__house = None    #отмечаем что у него на начальном этапе нет дома


    def info(self, name, age, money, house): #создаем функцию где выводим все о человеке
        print('имя', name, 'возраст', age, 'денег', money, 'дом', house, sep=" ")
    @staticmethod #и с помощью статического метода выводим информацию статических параметров
    def defoult_info():
        return Human.defolt_name, Human.defolt_age
"""












""" практика GIT , ЭТО КОМАНДА ПРИГОДИТЬСЯ КОГДА ОГРОМНЫЙ ПРОЕКТ И ЧТОБЫ СТРЕЛОЧКА ЗАПУСКА БЫЛА НА КОМАНДНОЙ ЛИНИИ
def plus(a, b):
    return a + b
if __name__ == "__main__":
    print(plus(5, 5))
"""



import random
import datetime
class User:
    name = " "
    sername = " "
    secondname = " "
    def __init__(self, name, sername, secondname):
        self.name = name
        self.sername = sername
        self.secondname = secondname


    def getFullName(self):
        print(f'{self.name}{self.sername} {self.secondname}')

class Student(User):
    year_of_admission = random.randint(1999, 2022)

    def __init__(self, name, sername, secondname, year_of_admission):
        super().__init__(name, sername, secondname)
        self.year_of_admission = year_of_admission


    def getFullName(self):
        return "Студент", super().getFullName(), "\nгод поступления", str(self.year_of_admission)


    def getCours(self):
        cours = int(datetime.datetime.now().year) - self.year_of_admission
        if cours <= 5:
            print(f"Он сейчас на {cours} курсе")
        else:
            print("Он у нас окончил обучение или еще не постШпал")

class Teacher(User):
    students = ["Юля", "Рома", "Миша", "Чурка"]
    def __init__(self, name, sername, secondname):
        super().__init__(name, sername, secondname)

    def getFullName(self):
        return super().getFullName()


    def Getstudents(self, students):
        print(list(students))


    def addstudents(self,students):
        return "мы добавили ", students.append()


    def removestudents(self, students):
        print(students.remove())
        if students in "Рома":
            print("Он остался там")
        else:
            print("Мы проверили, его там нет")
St = User("Петренков", "Роман","Сергеевич")
St1 = Student("Петренков", "Роман","Сергеевич", Student.year_of_admission)
Tch = Teacher("Людмила", "Мамедова", "Борисовна")
print("Имя студента", St.name, St.sername, St.secondname, St1.year_of_admission)
print(St1.getCours())
print(Tch.getFullName())
print("у нашего учителя были", Tch.students)
print("Добавиои к нашему учителю", Tch.students.append("рака"))
print(Tch.students)
print("Мы удалили Рому", Tch.students.remove("МИША"))
print(Tch.students)