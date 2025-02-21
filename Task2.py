class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def introduce(self):
        print(f"Hi, I'm {self.name}. an {self.age} year-old {self.course} student.")

student1 = Student("Rica",25, "Hospitality Management")
student2 = Student("Maria", 19, "Bachelor of Arts in English Language")
student3 = Student("Khanng", 21, "Information Technology")

print("Student 1:")
student1.introduce()
print("\nStudent 2:")
student2.introduce()
print("\nStudent 3:")
student3.introduce()
