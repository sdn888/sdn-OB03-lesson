class Teacher():
    def teach(self):
        print("A teacher teaches pupils")

class School():
    def __init__(self, new_teacher):
        self.teacher = new_teacher

    def start_lesson(self):
        self.teacher.teach()

my_teacher = Teacher()
my_school = School(my_teacher)

my_teacher.teach()
my_school.start_lesson()


