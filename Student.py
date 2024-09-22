class Student:
    def __init__(self, name, age, year):
        self.name = name
        self.age = age
        self.year = year
        self.subjects = []
        self.grades = {}
        self.wallet = 0

    def __str__(self):
        return f'Student - {self.name}'

    def __repr__(self):
        return f'The object Student - {self.name}'

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    def __lt__(self, other):
        return self.age < other.age

    def __ne__(self, other):
        return not self.__eq__(other)
    
    def add_subject(self, subject):
        self.subjects.append(subject)
        self.grades[subject] = []

    def add_grade(self, subject, grade):
        if subject in self.subjects:
            self.grades[subject].append(grade)
        else:
            print("There is no this subject in students list")

    def average_grade(self, subject):
        if subject in self.grades:
            return (sum(self.grades[subject]) / len(self.grades[subject]))
        else:
            return None

    def describe_yourself(self):
        print(f"Hello! I am {self.name}.",
              f"I am {self.age} years old.",
              f"I am on the {self.year} year of my education.")



class StudentPreschool(Student):
    def __init__(self, name, age, year):
        super().__init__(name, age, year)
        self.year=0

    def count_till(self):
        print(f"{self.name} will go to the elementary school in {5-self.age} years!")

class Student_Elementary(Student):
    def lunchbox_unpacking(self):
        a=input('Hey, your mommy cooked something tasty for you today!Right? Enter - Yes or No --->')
        if a == 'Yes':
            print("Grilled sandwich was taking sights from everyone in your canteen")
        else:
            print("You have died from hunger")

class Student_Middle(Student_Elementary):
    def driving(self):
        print("Hello! Its your driving test! First of all say some words about yourself")
        super().describe_yourself()
        a=[int(i) for i in (input("Nice! So the only one question - show me your credit card numbers--->").split())]
        b=0
        for i in a:
            b += i
        if b>= 11000:
            print('Well done! Here is your driving licence!')
        else:
            print('Well, try next year...')

class Student_High(Student):
    def describe_yourself(self):
        print("No, i dont want.")
