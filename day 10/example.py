class Parent():
    a = 10 
    b = 11 
    def __init__(self):
        print("Parent class initialized")
    
    def add(self):
        return self.a + self.b
    
class Child(Parent):
    def __init__(self):
        print("Child class initialized")
        Parent.__init__(self) # calling parent class constructor
        super().__init__() # calling parent class constructor using super()
    
    def result(self):
      return {
        "a": self.a,
        "b": self.b,
        "sum": self.add()
    }
  
    
obj = Child()
print(obj.result())
print(obj.add())


class Employee():
    def __init__(self, employee_id, name, salary):
        self.employee_id = employee_id
        self.name = name
        self.salary = salary
    def employee_details(self):
        return f"Employee ID: {self.employee_id}"

class Manager(Employee):
    bonus = 9000
    def total_salary(self):
        total = self.salary + self.bonus
        return f"Total Salary: {total}"
    
obj = Manager(1, "Nischal", 50000)
print(obj.employee_details())
print(obj.total_salary())
            
            
class Teacher():
    def __init__(self, teacher_name, subject):
        self.teacher_name = teacher_name
        self.subject = subject

    def teacher_lesson(self):
        return self.subject
    
class ContentCreator():
    def __init__(self, channel_name):
        self.channel_name = channel_name

    def upload_video(self):
        return self.channel_name + "Python class"
    
class OnlineEducator(Teacher, ContentCreator):
    def __init__(self, teacher_name, subject, channel_name):
        Teacher.__init__(self, teacher_name, subject)
        ContentCreator.__init__(self, channel_name)

    def show_profile(self):
        return f"Teacher Name: {self.teacher_name}, Subject: {self.subject}, Channel Name: {self.channel_name}"
    
obj = OnlineEducator("Nischal", "Maths", "Nischal Tech")
print(obj.show_profile())
print(obj.upload_video())


