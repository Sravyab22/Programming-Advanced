class student:
    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade
    def get_grade(self):
        return self.grade
s1=student("Tara",18,95)
s2=student("Rahul",19,90)
print(s1.age)
print(s2.name)
print(s1.get_grade())
print(s2.get_grade())

print(s1.__dict__)
print(s2.__dict__)

class Course:
    def __init__(self,name,max_students):
        self.name=name
        self.max_students=max_students
        self.students=[]
    def add_students(selfself,student):
        if(len(self.students)< self.max_students):
            self.students.append(student)
            self.students=[]
            return true
        return false
        pass

    def avg_grade(self):
        value=0
        for s in self.students:
            value=value+s.get_grade()
            pass
        return value/len(self.students)

course= Course("Computer",4)
course= Course("Biology",6)
print(course.__dict__)

print(course.add_students(s1))
print(course.add_students(s2))


