class Kassa:
    def __init__(self, money):
        self.money=money
    def top_up(self, x):
        self.money+=x
    def count_1000(self):
        print(self.money//1000)
    def take_away(self, x):
        if x>self.money:
            print('Ошибка')
        else:
            self.money-=x
    def get_money(self):
        print(self.money)
print('Введите количество денег в кассе')
x=int(input())
k=Kassa(x)
k.get_money()
k.count_1000()
print('Пополняем кассу')
y=int(input())
k.top_up(y)
k.get_money()
k.count_1000()
print('Забираем с кассы')
s=int(input())
k.take_away(s)
k.get_money()
k.count_1000()