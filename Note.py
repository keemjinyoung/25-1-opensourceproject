class Student:
    def init(self, num, name, eng, c, py, sum, aver, grade, rank):
        self.num = num
        self.name = name
        self.eng = eng
        self.c = c
        self.py = py
        self.sum = sum
        self.aver = aver
        self.grade = grade
        self.rank = rank

    def input_Student(self):
        num = int(input("학번 : "))
        name = input("이름 : ")
        eng = int(input("영어 : "))
        c = int(input("C-언어 : "))
        py = int(input("파이썬 : "))
        sum = eng+c+py
        aver = sum/3

    def get_rank(self):
        get_ranking()

    def repr(self):
        return repr((self.num, self.name, self.eng, self.c, self.py, self.sum, self.aver, self.grade, self.rank))
    

    
a = Student()
b = Student()
c = Student()
d = Student()
e = Student()

student_objects = [a, b, c, d, e]

def get_ranking():
    sorted(student_objects, key=lambda student: student.sum) [a, b, c, d, e]