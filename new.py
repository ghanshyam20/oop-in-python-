class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []  # list of numbers

    def add_grade(self, g):
        self.grades.append(g)

    def average(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0.0

s = Student("Asha")
s.add_grade(90); s.add_grade(78)
print(s.name, s.average())
