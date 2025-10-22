from classroom import ClassRoom
from person import Student, Teacher
from school import School
from subject import Subject

school = School("ABC Primary School", "Dhaka, Bangladesh")

one = ClassRoom("One")
two = ClassRoom("Two")
three = ClassRoom("Three")
four = ClassRoom("Four")
five = ClassRoom("Five")

school.add_classroom(one)
school.add_classroom(two)
school.add_classroom(three)
school.add_classroom(four)
school.add_classroom(five)

arnab = Student("Arnab Saha", five)
suchi = Student("Suchi Dhar", five)
riya = Student("Riya Saha", four)
ridom = Student("Ridom Saha", three)
ritu = Student("Ritu Saha", two)
arna = Student("Arna Saha", one)
joyta = Student("Joyta Saha", one)
asses = Student("Asses Saha", two)

school.student_admission(arnab)
school.student_admission(suchi)
school.student_admission(riya)
school.student_admission(ridom)
school.student_admission(ritu)
school.student_admission(arna)
school.student_admission(joyta)
school.student_admission(asses)


subrata = Teacher("Subrata Saha")
ratna = Teacher("Ratana Banarjee")
satabdi = Teacher("Sabtabdi Roy")
tonmoy = Teacher("Tonmoy Saha")
arup = Teacher("Arup Ratan")

bangla = Subject("Bangla", tonmoy)
math = Subject("Math", subrata)
english = Subject("English", arup)
art = Subject("Art", satabdi)
general_knowledge = Subject("General Knowledge", ratna)

one.add_subject(bangla)
one.add_subject(math)
one.add_subject(general_knowledge)

two.add_subject(bangla)
two.add_subject(math)
two.add_subject(english)

three.add_subject(math)
three.add_subject(english)
three.add_subject(art)

four.add_subject(math)
four.add_subject(english)
four.add_subject(art)

five.add_subject(english)
five.add_subject(math)
five.add_subject(general_knowledge)


one.final_exam()
two.final_exam()
three.final_exam()
four.final_exam()
five.final_exam()

print(school)
