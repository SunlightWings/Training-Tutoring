class Student:

  def __init__(self, name, age, grade):
    self.name = name
    self.age = age
    self.grade = grade


  def introduction(self):
    print(f"Hello, I am {self.name}. I am {self.age} years old. I got {self.grade} in my school")

## Instantiation
s2 = Student("Alice", 'Twelve', 3.89)

print(s2.name)
print("\n")
print(s2.introduction())