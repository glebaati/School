from faker import Faker
fake = Faker("ru_RU")

class Ticket:
    def __init__(self, author):
        self.author = author
        self.difficult_level = 'easy'
        self.additional_questions = []
        self.dean_signed = False

    def generate_ticket(self, GroupName, subject, count):
        if 3 < GroupName.average_group_grade(subject) < 4:
            self.difficult_level = 'normal'
        elif GroupName.average_group_grade(subject) < 3:
            pass
        else:
            self.difficult_level = 'hard'
        for i in range(count):
             yield fake.text(), self.author, self.difficult_level, f'Подпись декана - {self.dean_signed}'

    def generate_additional_questions(self, count):
        for i in range(count):
            yield self.additional_questions.append(fake.text())

    def sign_be_dean(self):
        self.dean_signed = True