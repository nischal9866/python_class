#access modifier - public, private, protected

class Test():
    a = 100
    __b = 2    # this variable is private and cannot be accessed outside the class
    
    def add(self):
        return self.a + self.__b
    
obj = Test()
print(obj.add())
    
    