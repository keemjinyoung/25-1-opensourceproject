'''board= [[' ' for x in range (3)] for y in range(3)]

while True:
# 게임 보드를 그린다.
    for r in range(3):
        print("  " + board[r][0] + "|  " + board[r][1] + "|  " + board[r][2])
        if (r != 2):
            print("---|---|---")

# 사용자로부터 좌표를 입력받는다.
    x = int(input("다음 수의 x좌표를 입력하시오: "))
    y = int(input("다음 수의 y좌표를 입력하시오: "))

# 사용자가 입력한 좌표를 검사한다.
    if board[x][y] != ' ':
        print("잘못된 위치입니다. ")
        continue
    else:
        board[x][y] = 'X'

#컴퓨터가 놓을 위치를 결정한다. 첫 번째로 발견하는 비어있는 칸에 놓는다.
    done = False
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ' and not done:
                board[i][j] = 'O'
                done = True
                break'''

# 보드판 생성
board = [[' ' for _ in range(3)] for _ in range(3)]

def print_board():
    for i in range(3):
        print(" " + board[i][0] + " | " + board[i][1] + " | " + board[i][2])
        if i != 2:
            print("---|---|---")

def finish():
    # 가로, 세로 검사
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != " ":
            print(f"<<{board[i][0]}>>가 이겼습니다!")
            return False
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != " ":
            print(f"<<{board[0][i]}>>가 이겼습니다!")
            return False

    # 대각선 검사
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        print(f"<<{board[0][0]}>>가 이겼습니다!")
        return False
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        print(f"<<{board[0][2]}>>가 이겼습니다!")
        return False

    # 무승부 검사
    if all(cell != " " for row in board for cell in row):
        print("무승부입니다!")
        return False

    return True

print("Welcome Tic-Tac-Toe game!")

while True:
    print_board()
    print("\n왼쪽 위부터 → x좌표 0,1,2 / ↓ y좌표 0,1,2")
    print("유저가 둔 수 : X / 컴퓨터가 둔 수 : O")

    try:
        x = int(input("다음 수의 x 좌표 선택 (0-2): "))
        y = int(input("다음 수의 y 좌표 선택 (0-2): "))
    except ValueError:
        print("잘못된 입력입니다. 숫자를 입력하세요.")
        continue

    if x not in [0,1,2] or y not in [0,1,2]:
        print("잘못된 위치입니다. 0~2 사이의 값을 입력하세요.")
        continue

    if board[y][x] != " ":
        print("이미 선택된 자리입니다. 다시 시도하세요.")
        continue

    # 유저(X) 입력
    board[y][x] = 'X'

    # 게임 종료 여부 확인
    if not finish():
        print_board()
        break

    # 컴퓨터(O) 입력 (첫 번째 빈 칸을 찾음)
    done = False
    for i in range(3):
        for j in range(3):
            if board[i][j] == " " and not done:
                board[i][j] = 'O'
                done = True
                break

    # 게임 종료 여부 확인
    if not finish():
        print_board()
        break
