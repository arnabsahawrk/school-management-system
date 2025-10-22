from school import School


class Subject:
    def __init__(self, name, teacher) -> None:
        self.name = name
        self.teacher = teacher
        self.max_marks = 100
        self.pass_marks = 33

    def exam(self, students):
        for student in students:
            mark = self.teacher.evaluate_exam()
            student.subjects_mark[self.name] = mark
            student.subjects_grade[self.name] = School.calculate_grade(mark)
