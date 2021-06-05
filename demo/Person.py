class Person:
    name = "小甲鱼"
    __name = "小甲鱼"
    def getName(self):
        return self.__name
if __name__ == '__main__':
    from turtle import Turtle
    p = Person()
    print(p.name)
    P = Person
    P.getName()
    p.__Person__name