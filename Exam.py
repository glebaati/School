class Exam:
    def __init__(self):
        self.date = None
        self.teacher = None
        self.tickets = []
        self.group = None
        self.subject = None

    def set_date(self, date):
        self.date = date

    def set_teacher(self, teacher):
        self.teacher = teacher

    def set_group(self, GroupName):
        self.group = GroupName

    def set_subject(self, subject):
        self.subject = subject

    def generate_and_add_tickets(self, ticket, count):
        generated_tickets = ticket.generate_ticket(self.group, self.subject, count)
        for generated_ticket in generated_tickets:
            self.tickets.append(generated_ticket)

    def get_all_tickets(self):
        return self.tickets

    def count_tickets(self):
        return len(self.tickets)

    def set_grade(self, student, grade):
        student.add_grade(self.subject, grade)