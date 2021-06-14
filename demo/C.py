class C:
    def __init__(self, size=10):
            self.size = size
    def getSize(self):
            return self.size
    def setSize(self, value):
            self.size = value
    def delSize(self):
        del self.size
    x = property(getSize, setSize, delSize)
if __name__ == '__main__':
    c1 = C()
    print(c1.getSize())
    c1.x = 10
    c1.x