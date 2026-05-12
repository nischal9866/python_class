#multipe inheritance 
#in single inheritance we habe one parent class and one child class but in multiple inheritance we have more than one parent class and one child class

class A():
    a = 10 

class B():
    b = 100

class C(B, A):
    d = 1000
    
print(C.__mro__)
obj = C()
print(obj.a)

class Employee():
    employee_id = 77
    employee_name = "Hari"
    basic_salary = 750
    
class Manager():
    bonus = 9000
    
class Boss(Employee, Manager):
    def total_salary(self):
        return self.basic_salary + self.bonus
    
obj = Boss()
print(obj.total_salary())