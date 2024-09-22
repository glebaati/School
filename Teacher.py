class Teacher:
    def __init__(self, name):
        self.name = name
        self.subjects = []

    def add_subject(self, subject):
        if subject not in self.subjects:
            self.subjects.append(subject)
            subject.set_teacher(self)