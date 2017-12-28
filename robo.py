class Robot:
    '''Robot class'''
    def __init__(self,name=None):
        '''init method for taking the name'''
        self.name = name

    def say_hello(self):
        if self.name:
            print("Hello, I am "+self.name)
        else:
            print("Hello, I am Robo without a name")

if __name__ =="__main__":
    x = Robot()
    y = Robot()
    print(x==y)
    y1 = y
    print(y==y1)
    print(help)
