import random

from school import School


class Person:
    def __init__(self, name) -> None:
        self.name = name


class Teacher(Person):
    def __init__(self, name) -> None:
        super().__init__(name)

    def evaluate_exam(self):
        return random.randint(0, 100)


class Student(Person):
    def __init__(self, name, classroom) -> None:
        super().__init__(name)
        self.classroom = classroom
        self.__id = None
        self.subjects_mark = {}
        self.subjects_grade = {}
        self.grade = None

    def final_grade(self):
        sum = 0

        for grade in self.subjects_grade.values():
            point = School.grade_to_value(grade=grade)
            sum += point

        if len(self.subjects_grade):
            gpa = sum / len(self.subjects_grade)
        else:
            gpa = 0.00

        self.grade = School.value_to_grade(gpa)

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value
