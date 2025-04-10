# 성적관리 프로그램 II
# 2022078005 김진영
# 2025.03.29



#총점/평균 계산 함수
def sum(eng, c, py):
    sum_result = eng + c + py
    aver = float(sum_result / 3)
    return sum_result, aver

#학점 계산 함수
def grade(aver_for_grade):
    grade = ""
    if(aver_for_grade >= 95):
        grade = "A+"
    elif(aver_for_grade >= 90) :
        grade = "A"
    elif(aver_for_grade >= 85) :
        grade = "B+"
    elif(aver_for_grade >= 80) :
        grade = "B"
    elif(aver_for_grade >= 75) :
        grade = "C+"
    elif(aver_for_grade >= 70) :
        grade = "C"
    elif(aver_for_grade >= 65) :
        grade = "D+"
    elif(aver_for_grade >= 60) :
        grade = "D"
    else :
        grade = "F"
    return grade

scores = [] # 점수 리스트
overaver = [] # 80점 넘는 학생 리스트

#학생 1의 점수 입력 함수 (입력, 삽입 함수)
num_1 = int(input("학번 : "))
name_1 = input("이름 : ")
score_eng_1 = int(input("영어 : "))
score_c_1 = int(input("C-언어 : "))
score_py_1 = int(input("파이썬 : "))
sum_1, aver_1 = sum(score_eng_1, score_c_1, score_py_1)
grade_1 = grade(aver_1)
scores.append([name_1, aver_1]) # 리스트에 학생 이름과 평균 점수 삽입
overaver.append(aver_1)

#학생 2의 점수 입력 함수
num_2 = input("학번 : ")
name_2 = input("이름 : ")
score_eng_2 = int(input("영어 : "))
score_c_2 = int(input("C-언어 : "))
score_py_2 = int(input("파이썬 : "))
sum_2, aver_2 = sum(score_eng_2, score_c_2, score_py_2)
grade_2 = grade(aver_2)
scores.append([name_2, aver_2])
overaver.append(aver_2)

#학생 3의 점수 입력 함수
num_3 = input("학번 : ")
name_3 = input("이름 : ")
score_eng_3 = int(input("영어 : "))
score_c_3 = int(input("C-언어 : "))
score_py_3 = int(input("파이썬 : "))
sum_3, aver_3 = sum(score_eng_3, score_c_3, score_py_3)
grade_3 = grade(aver_3)
scores.append([name_3, aver_3])
overaver.append(aver_3)

#학생 4의 점수 입력 함수
num_4 = input("학번 : ")
name_4 = input("이름 : ")
score_eng_4 = int(input("영어 : "))
score_c_4 = int(input("C-언어 : "))
score_py_4 = int(input("파이썬 : "))
sum_4, aver_4 = sum(score_eng_4, score_c_4, score_py_4)
grade_4 = grade(aver_4)
scores.append([name_4, aver_4])
overaver.append(aver_4)

#학생 5의 점수 입력 함수
num_5 = input("학번 : ")
name_5 = input("이름 : ")
score_eng_5 = int(input("영어 : "))
score_c_5 = int(input("C-언어 : "))
score_py_5 = int(input("파이썬 : "))
sum_5, aver_5 = sum(score_eng_5, score_c_5, score_py_5)
grade_5 = grade(aver_5)
scores.append([name_5, aver_5])
overaver.append(aver_5)


# 등수 계산 함수 (정렬 함수)
scores.sort(key = lambda x:x[1], reverse=True)
def get_rank(scores, name) :
    for i in range(5) :
        if scores[i][0] == name :
            return i+1
        

# 80점이상 학생 수 카운트 함수(평균 80점 넘지 않는 학생 삭제)
overaver.sort(reverse=True)
while(overaver[-1]) :
        if overaver[-1] < 80 :
            overaver.pop(-1)
        else :
            break


#출력 함수
print("\n\n             성적관리 프로그램")
print("===========================================================================")
print("학번	    이름\t영어\tC-언어\t파이썬\t총점\t평균\t학점\t등수")
print("===========================================================================")
print(num_1, name_1+ "\t", score_eng_1, "\t", score_c_1, "\t", score_py_1, "\t", sum_1, "\t", "%.2f" %aver_1, "\t", grade_1, "\t", get_rank(scores, name_1))
print(num_2, name_2+ "\t", score_eng_2, "\t", score_c_2, "\t", score_py_2, "\t", sum_2, "\t", "%.2f" %aver_2, "\t", grade_2, "\t", get_rank(scores, name_2))
print(num_3, name_3+ "\t", score_eng_3, "\t", score_c_3, "\t", score_py_3, "\t", sum_3, "\t", "%.2f" %aver_3, "\t", grade_3, "\t", get_rank(scores, name_3))
print(num_4, name_4+ "\t", score_eng_4, "\t", score_c_4, "\t", score_py_4, "\t", sum_4, "\t", "%.2f" %aver_4, "\t", grade_4, "\t", get_rank(scores, name_4))
print(num_5, name_5+ "\t", score_eng_5, "\t", score_c_5, "\t", score_py_5, "\t", sum_5, "\t", "%.2f" %aver_5, "\t", grade_5, "\t", get_rank(scores, name_5))
print("===========================================================================")
print("평균 80점 넘는 학생 수 : ", len(overaver))