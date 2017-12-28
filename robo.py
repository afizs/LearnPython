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

    def set_name(self, name): # Data Encapsulation 
        self.name = name

    def get_name(self): # Data Encapsulation
        return self.name

if __name__ =="__main__":
    x = Robot('arjunaa')
    y = Robot()
    print(x.say_hello())
    print(y.say_hello())
    
