# class Person():
#     a=10
#     b=11

# obj1=Person()
# print(obj1.a)

# obj1=Person()
# obj1.a = 77
# print(obj1.a)

# obj2=Person()
# print(obj2.a)


class Math():
    def __init__(self,a, b):
        print(a,b)
        self.a = a 
        self.b = b
        print(" i am constructor")
    
    def add(self):
        return self.a + self.b
    
    def sub(self):
        return self.a - self.b
    def result(self):
        self.c = "hello world"
        print(self.a)
        print(self.add())
        print(self.sub())
    
obj = Math(10, 20)

print(obj.add())
obj.result()
obj.sub()
print(obj.c)
