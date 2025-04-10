  # Score_III
  # 소프트웨어학부 2022078005 김진영
  # 2025.04.10
  # 객체지향을 이용한 성적관리 프로그램


#Class 1 학생 정보
class Student :
    def __init__(self, id, name, eng, c, py, sum) :
        self.id = id
        self.name = name
        self.eng = eng
        self.c = c
        self.py = py
        self.sum = sum
        self.aver = self.sum/3
        self.grade = self.for_grade()

    # 학점 계산 함수
    def for_grade(self) :
        aver = self.aver
        if(aver >= 95) : return "A+"
        elif(aver >= 90) : return "A"
        elif(aver >= 85) : return "B+"
        elif(aver >= 80) : return "B"
        elif(aver >= 75) : return "C+"
        elif(aver >= 70) : return "C"
        elif(aver >= 65) : return "D+"
        elif(aver >= 60) : return "D"
        else : return "F"


#Class 2 학생끼리 정보 비교
class Compare :
    def __init__(self) :
        self.students = [] # 학생 각각의 정보 담을 리스트 생성

    # 학생 각각의 정보 수집
    def set_info(self):
        for i in range (5) :
            id = int(input("학번 : "))
            name = input("이름 : ")
            eng = int(input("영어 : "))
            c = int(input("C-언어 : "))
            py = int(input("파이썬 : "))
            sum = eng+c+py
            student = Student(id, name, eng, c, py, sum)
            self.students.append(student)

    # 등수 측정
    def for_rank(self) :
        self.students.sort(key = lambda x:x.aver, reverse=True) # 평균 점수를 이용해 등수 정렬

    # 출력 함수
    def print_score(self) :
        self.for_rank()
        print("\n\n             성적관리 프로그램")
        print("===========================================================================")
        print("학번	    이름\t영어\tC-언어\t파이썬\t총점\t평균\t학점\t등수")
        print("===========================================================================")
        for i, student in enumerate(self.students) : # enumerate 함수를 이용해 학생의 정보와 등수를 함께 출력
            print(f"{student.id} {student.name}\t{student.eng}\t{student.c}\t{student.py}\t{student.sum}\t{student.aver:.2f}\t{student.grade}\t{i+1}")


# 메인 함수
if __name__ == "__main__" :
    run = Compare()
    run.set_info()
    run.for_rank()
    run.print_score()