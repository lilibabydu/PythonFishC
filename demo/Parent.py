class Parent:
    def hello(self):
            print("正在调用父类的方法...")
class Child(Parent):
    def hello(self):
            print("正在调用子类的方法...")            
if __name__ == '__main__':
    from turtle import Turtle
    p = Parent()
    p.hello()
    c = Child()
    c.hello()