class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age 

    def introduce(self):
        return f"I am {self.name}, a person."

class Student(Person):  # Inheritance
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def introduce(self):
        return f"I am {self.name}, a student with ID: {self.student_id}."

print("\n--- Task 3 Output ---")
p = Person("John", 40)
s = Student("Jane", 20, "S12345")

people = [p, s]
for person in people:
    print(person.introduce())