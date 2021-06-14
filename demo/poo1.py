class Turtle:
    def __init__(self, x):
        self.num = x
class Fish:
    def __init__(self, x):
        self.num = x
class Poo1:
    def __init__(self, x, y):
        self.turtle = Turtle(x)
        self.fish = Fish(y)
    def print_num(self):
        print("水池里总共有乌龟 %d 只，小鱼 %d 条！" % (self.turtle.num, self.fish.num)) 
if __name__ == '__main__':
    # from turtle import Turtle
    poo1 = Poo1(1, 10)
    poo1.print_num()           
