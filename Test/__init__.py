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

    def __make_idea(self, home, price):
        self.__house = home
        self.__money -= price

    def earn_money(self, plus):
        self.__money += plus
    print('Hello,your on credited -->>>', 'руб ')

    def buy_house(self,home, diskord ):
