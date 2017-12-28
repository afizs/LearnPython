class Robot:
    '''Robot class'''
    def __init__(self,
                 name=None,
                 build_year=None):
        '''init method for taking the name'''
        self.name = name
        self.build_year = build_year

    def say_hello(self):
        if self.name:
            print("Hello, I am "+self.name)
        else:
            print("Hello, I am Robo without a name")

        if self.build_year:
            print("Hello, I was built in the year "+ self.build_year)
        else:
            print("Hello, Nobody knows about my built year")


    def set_name(self, name): # Data Encapsulation 
        self.name = name

    def get_name(self): # Data Encapsulation
        return self.name

    def set_build_year(self, year):
        self.build_year = year

    def get_build_year(self):
        return self.build_year

if __name__ =="__main__":
    x = Robot('arjunaa')
    x.set_build_year("2017")
    y = Robot()
    print(x.say_hello())
    print(y.say_hello())
    
