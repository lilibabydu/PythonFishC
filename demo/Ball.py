class Ball:
    '''
    Ball class
    '''
    def __init__(self, name='武术'):
           self.name = name
    def kick(self): 
            print("我叫%s，该死的，谁打我..." % self.name)     
    def setName(self, name):
           self.name = name
    def kick(self):
        print("我叫%s，该死的，谁打我..." % self.name)

          
if __name__ == '__main__':
    from turtle import Turtle
    # a = Ball('')
    # a.setName('球A')
    # b = Ball()
    # b.setName('球B')
    # c = Ball()
    # c.setName('土豆')
    # a.kick()
    # c.kick()
    b = Ball('土豆')
    b.kick()

    d = Ball()
    d.kick()
    


    


