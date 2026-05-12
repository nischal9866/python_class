class Student():
    def __init__(self, name, roll_no, *marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
    def average(self):
        return sum(self.marks) / len(self.marks)
    def grade(self):
        avg = self.average()
        print(avg)
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"
        
student1 = Student("Nischal", 12, 90,10)
print(student1.grade())
