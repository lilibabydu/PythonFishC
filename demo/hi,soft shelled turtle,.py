class Turtle:
    """关于类的一个简单例子"""
    color = 'green'
    weight = 10
    legs = 4
    shell = True
    mouth = '大嘴'
    def climb(self):
        print("我正在很努力的向往爬......")
    def run(self):
        print("我正在飞快的向前跑......")
    def bite(self):
        print("咬死你咬死你！！")
    def eat(self):
        print("有的吃，真满足^_^")
    def sleep(self):
        print("困了，睡了，晚安，Zzzz") 


print(__name__)
if __name__ =='__main__':
    tt = Turtle()
    tt.climb()
    tt.bite()
    tt.sleep()
    tt.eat()
    pass
