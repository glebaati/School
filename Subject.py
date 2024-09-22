class Subject:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher
        self.students = []

    def set_teacher(self, teacher):
        self.teacher = teacher

    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)
            student.add_subject(self)