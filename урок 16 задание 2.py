class Turtle:
    def __init__(self, x, y, s):
        self.x=x
        self.y=y
        self.s=s
    def go_up(self):
        self.y+=self.s
    def go_down(self):
        self.y-=self.s
    def go_left(self):
        self.x-=self.s
    def go_right(self):
        self.x+=self.s
    def evolve(self):
        self.s+=1
    def degrade(self):
        self.s-=1
    def count_moves(self, x2, y2):
        return (x2-self.x)/self.s, (y2-self.y)/self.s
print('Создаём черепашку x, y, s')
x, y, s= map(int, input().split())
t=Turtle(x, y, s)
print('Вычисляем количество шагов до точки х2 у2')
x2, y2= map(int, input().split())
r=t.count_moves(x2, y2)
print(f'По x {r[0]} и по y {r[1]}')
