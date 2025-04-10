
# 클래스 1(학생 정보)
class Students :
    def init(self, id, name, eng, c, py, sum, aver, grade, rank):
        self.id = id
        self.name = name
        self.eng = eng
        self.c = c
        self.py = py
        self.sum = sum
        self.aver = aver
        self.grade = grade
        self.rank = rank

    # 총점 계산 함수
    def for_sum(eng, c, py):
        sum = eng + c + py
        return sum
    
    # 평균 계산 함수
    def aver(sum):
        aver = float(sum / 3)
        return aver
    
    # 학점 계산 함수
    def grade(aver):
        if(aver >= 95) : return "A+"
        elif(aver >= 90) : return "A"
        elif(aver >= 85) : return "B+"
        elif(aver >= 80) : return "B"
        elif(aver >= 75) : return "C+"
        elif(aver >= 70) : return "C"
        elif(aver >= 65) : return "D+"
        elif(aver >= 60) : return "D"
        else : return "F"
    
    # 출력 함수
    def show(self):
        print(self.num, self.name, "\t", self.eng, "\t", self.c, "\t", self.py,
              "\t", self.sum, "\t", self.aver, "\t", self.grade, "\t", self.rank)


def set_info():
    id = int(input("학번 : "))
    name = input("이름 : ")
    eng = int(input("영어 : "))
    c = int(input("C-언어 : "))
    py = int(input("파이썬 : "))
    scores.append([name, eng+c+py])

def sort_scores(self):
    scores.sort(key = lambda x:x[1], reverse=True)
    def rank(scores, name) :
        for i in range(5) :
            if scores[i][0] == name :
                return i+1
    

scores = []
a = Students()
b = Students()
c = Students()
d = Students()
e = Students()




#출력 함수
print("\n\n             성적관리 프로그램")
print("===========================================================================")
print("학번	    이름\t영어\tC-언어\t파이썬\t총점\t평균\t학점\t등수")
print("===========================================================================")
a.show()