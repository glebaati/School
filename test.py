import Student, Group, Teacher, Subject, Ticket, Exam

x = Group.StudentsGroup('Nerds')
a = Student.Student('Кирилл', 18, 1)
a.add_subject('Math')
a.add_grade('Math', 5)
b = Student.Student('Настя', 18, 1)
b.add_subject('Math')
b.add_grade('Math', 3)
x.add_student(a)
x.add_student(b)
x.give_money()

z = Ticket.Ticket('Oleg')
s = z.generate_ticket(x,'Math', 10)

exam = Exam.Exam()
exam.set_date("01.06.2024")
exam.set_teacher("Преподаватель Иванов")
exam.set_group(x)
exam.set_subject("Math")
exam.generate_and_add_tickets(z, 5)
print(exam.get_all_tickets())
print(exam.count_tickets())
v = Student.Student('Миша', 19, 2)

try:
    student1 = Student.Student("Иван", 18, 1)
    student2 = Student.Student("Мария", 19, 1)
    group = Group.StudentsGroup("Группа 1")
    group.add_student(student1)

    group.kick_student(student2)
except Group.StudentAbsenceError as e:
    print(e)