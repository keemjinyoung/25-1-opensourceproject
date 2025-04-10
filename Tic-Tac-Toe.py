# Tic-Tac-Toe 프로그램
# 2022078005 김진영
# 2025.03.29


# 게임이 끝날 조건
def finish():
    # 가로, 세로 검사
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] == "X":
            print("<<User>>가 이겼습니다!")
            return False
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] == "O":
            print("<Computer>>이 이겼습니다!")
            return False
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] == "X":
            print("<<User>>가 이겼습니다!")
            return False
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] == "O":
            print("<<Computer>>이 이겼습니다!")
            return False

    # 대각선 검사
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] == "X":
        print("<<User>>가 이겼습니다!")
        return False
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] == "O":
        print("<<Computer>>이 이겼습니다!")
        return False
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] == "X":
        print("<<User>>가 이겼습니다!")
        return False
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] == "O":
        print("<<Computer>>이 이겼습니다!")
        return False

    # 무승부 검사
    if all(cell != " " for row in board for cell in row):
        print("무승부입니다!")
        return False

    return True


# 보드판 생성
board = [[' ' for x in range(3)] for y in range(3)]

print("Welcome to Tic-Tac-Toe game!")
while(True) :
    for i in range(3) :
        print(" " +board[i][0]+ " | " +board[i][1]+ " | " +board[i][2])
        if i != 2 :
            print("---|---|---")


# 유저에게 자리 선택
    print("왼쪽 위부터 → x좌표 0,1,2 / ↓ y좌표 0,1,2")
    print("유저가 둔 수 : X / 컴퓨터가 둔 수 : O")
    x = int(input("다음 수의 x 좌표 선택 : "))
    y = int(input("다음 수의 y 좌표 선택 : "))
    print("\n")


# 보드판에 자리 놓기
    if board[y][x] != " " :
        print("잘못된 위치입니다.")
        continue
    else :
        board[y][x] = 'X'
    #finish()
    if not finish() :
        break


# 컴퓨터가 자리 선택
    done = False
    for i in range(3) :
        for j in range(3) :
            if board[i][j] == ' ' and not done:
                board[i][j] = 'O'
                done = True
                break
    #finish()
    if not finish() :
        break