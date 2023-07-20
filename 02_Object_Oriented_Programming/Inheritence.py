# parent class
class User:
    
    def __init__(self):
        self.name = 'saif'

    def login(self):
        return 'login'

# child class
class Student(User):

    def enroll(self):
        return 'enroll into the course'


u = User()
s = Student()

print(s.name)
print(s.login())
print(s.enroll())