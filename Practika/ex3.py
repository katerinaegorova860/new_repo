from Student import Student
from course_group import CourseGroup


student = Student("Анна", "Иванова", 25, "инженер по тестированию")
classmate1 = Student("Иван", "Петров", 27, "инженер по тестированию")
classmate2 = Student("Мария", "Сидорова", 24, "инженер по тестированию")
classmate3 = Student("Дмитрий", "Кузнецов", 26, "инженер по тестированию")

course_group = CourseGroup(student, [classmate1, classmate2, classmate3])
print(course_group)