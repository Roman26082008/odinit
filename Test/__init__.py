class Human:              #информация о человеке
    defolt_name = "nonaem"     #начальное положение ноунейм
    defolt_age = 0          #начальный возраст 0
    miner = 0
    def __init__(self, name = defolt_name, age = defolt_age):         #мы создали значение по умолчанию
        self.name = name
        self.age = age       #все здесь выводим
        self.__money = 0        #отмечаем что у него ноль денег (и мы создали приват параметр)
        self.__house = None    #отмечаем что у него на начальном этапе нет дома


    def info(self, name, age, money, house): #создаем функцию где выводим все о человеке
        print(f'имя{self.name}')
        print(f'возраст{self.age}')
        print(f'Деньги {self.__money}')
        print(f'Дом{self.__house}')


    @staticmethod #и с помощью статического метода выводим информацию статических параметров
    def defoult_info():
        print(Human.defolt_name, Human.defolt_age)


    def __make_idea(self, home, price): #создаем дом и цена дома
        self.__house = home
        self.__money -= price


    def earn_money(self, miner):# прибавка прибыли к своему кошельку
        self.__money += miner
    print('Hello,your on credited -->>>', miner, '\n>>>наш баланс ')

    def buy_house(self, home, disk): #достаточно денег ли для покупки дома, хватает ли средств
        price = home.final_price(disk) #длинная переменная цена со скидкой
        if self.__money >= price: #условие при том хватит или не хватит денег
           self.__make_idea(home, price)
           print("У вас достаточно денег для покупки дома")
        else:
           print("У вас недостаточно средсттв для покупки")
class Home:
    def __init__(self, area, price):
        self._area = area
        self._price = price


    def final_price(self, disk):             # в этом контексте мы вычислили финальную стоимость
        final_prise = self._price * (100 - disk) / 100
        print(f"Итоговая цена:{final_prise}")
        return final_prise
class Smallhouse(Home):
    defolt_S = 40


    def __init__(self, price):
        super().__init__(Smallhouse.defolt_S, price)
Human.defoult_info()
pvp = Human("roman", 15)
b = Smallhouse(1_000)
pvp.buy_house(b, 0)
pvp.earn_money(1_000_000)
pvp.buy_house(b, 10)

