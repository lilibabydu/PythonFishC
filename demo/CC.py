class CC:
    def __init__(self):
            print("我是__init__方法，我被调用了...")
    def __del__(self):
            print("我是__del__方法，我被调用了...")
if __name__ == '__main__': 
    c1 = CC()                     