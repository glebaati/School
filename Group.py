class StudentAbsenceError(ValueError):
    pass

class StudentsGroup:
    def __init__(self, GroupName):
        GroupName = list()
        self.GroupName = GroupName
        self.teacher = None

    def __str__(self):
        return f'Group -{self.GroupName}, teacher - {self.teacher}'

    def __iter__(self):
        return iter(self.GroupName)

    def __len__(self):
        return len(self.GroupName)

    def __contains__(self, student):
        return student in self.GroupName

    def add_student(self, student):
        if student not in self.GroupName:
            self.GroupName.append(student)
        else:
            raise ValueError(student, 'is already in the group')

    def kick_student(self, student):
        if student in self.GroupName:
            self.GroupName.remove(student)
        else:
            raise StudentAbsenceError(student, 'is not in the group')


    def kick_all(self):
        self.GroupName.clear()

    def give_money(self):
       for student in self.GroupName:
        if student.average_grade('Math') > 4.3:
            student.wallet += 4900
        else:
            student.wallet += 2900

    def set_teacher(self, teacher):
        self.teacher = teacher

    def average_group_grade(self, subject):
        grade = 0
        for student in self.GroupName:
            grade += student.average_grade(subject)
        return grade / len(self.GroupName)