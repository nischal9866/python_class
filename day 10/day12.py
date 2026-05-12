class Parent():
    a= 10 
    b = 15
    
class Child(Parent):
    b=99
    c=00
    
obj = Child()
print(obj.a) # 10
print(obj.b) # 99   



