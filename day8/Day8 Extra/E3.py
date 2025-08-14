class Person:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.__email = email

    def display_info(self):
        return f"{self.name} ({self.id})"

    def get_email(self):
        return self.__email

class Student(Person):
    def __init__(self, id, name, email, major, gpa):
        super().__init__(id, name, email)
        self.major = major
        self.gpa = gpa
        self.courses = []

    def enroll(self, course):
        self.courses.append(course)

    def __lt__(self, other):
        return self.gpa < other.gpa

    def __repr__(self):
        return f"Student({self.name}, GPA={self.gpa})"

class Professor(Person):
    def __init__(self, id, name, email, department, courses_teaching):
        super().__init__(id, name, email)
        self.department = department
        self.courses_teaching = courses_teaching

s1 = Student(1, "Omar", "omar@email.com", "CS", 3.5)
s2 = Student(2, "Lina", "lina@email.com", "AI", 3.8)
s1.enroll("Python")
s2.enroll("ML")
print(s1.display_info(), s1.get_email())
print(s2.display_info(), s2.get_email())
print(s1 < s2)
print(repr(s1))
print(repr(s2))
