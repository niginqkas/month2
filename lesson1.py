# class Transport:
#     def __init__(self, the_year, the_model, the_color):
#         self.year = the_year
#         self.model = the_model
#         self.color = the_color
#
#     def change_color(self, new_color):
#         print(f'Changed color from {self.color} to {new_color}')
#         self.color = new_color
#
#
# class PLane(Transport):
#     def __init__(self, the_year, the_model, the_color):
#         self.year = the_year
#         self.model = the_model
#         self.color = the_color
#
#     def change_color (self, new_color):

# class Car:
#     def __init__(self, the_model, the_year, the_color, penalties = 0):
#
#         self.model = the_model
#         self.year = the_year
#         self.color = the_color
#         self.penalties = penalties
#
# print('Start')
# number = 65
# bmw_car = Car('BMW X7', '2020', 'red')
# print(bmw_car)
# print(f'MODEL: {bmw_car.model} YEAR: {bmw_car.year}  '
#       f'COLOR: {bmw_car.color} PENALTIES: {bmw_car.penalties}')




# class Person:
#     def __init__(self, the_name, the_age):
#         self.name = the_name
#         self.age = the_age
#
#     def introduce_myself(self):
#         print(f'Name: {self.name}, Age: {self.age}')
#
#
#
# class Student(Person):
#     def __init__(self, name, age, marks):
#         super().__init__(name, age)
#         self.marks = marks
#
#
#     def average_mark(self):
#         total_marks = sum(self.marks.values())
#         subjects_count = len(self.marks)
#         return total_marks / subjects_count if subjects_count > 0 else 0
#
#
#     def introduce_myself(self):
#         super().introduce_myself()
#         for subject, mark in self.marks.items():
#             print(f'{subject}: {mark}')
#         print(f'Average mark: {self.average_mark()}')
#
#
#
# class Teacher(Person):
#     base_salary = 50000
#     def __init__(self, name, age, experience):
#         super().__init__(name, age)
#         self.experience = experience
#
#
#     def calculate_salary(self):
#         bonus_years = max(0, self.experience - 3)
#         bonus = self.base_salary * 0.05 * bonus_years
#         return self.base_salary + bonus
#
#
#     def introduce_myself(self):
#         super().introduce_myself()
#         print(f'Experience: {self.experience} years')
#         print(f'Salary: {self.calculate_salary()}')
#
#
#
# def create_students():
#     student1 = Student('Alim', 16, {'Math': 70, 'History': 85, 'Biology': 80})
#     student2 = Student('Aleksey', 18, {'Math': 75, 'History': 80, 'Chemistry': 85})
#     student3 = Student('Erjan', 17, {'Math': 80, 'Literature': 85, 'Biology': 95})
#
#     return [student1, student2, student3]
#
#
# students = create_students()
# for student in students:
#     student.introduce_myself()

#     print("-" *  30)

