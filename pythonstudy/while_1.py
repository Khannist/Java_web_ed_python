#나무 찍기
#while_1.py


treeHit = 0 # 나무를 찍은 횟수
while treeHit < 10: # 나무를 찍은 횟수가 10보다 작은 동안 반복
                    # treeHit < 10 조건에 만족할때만 아래로 내려감.
                    # 그렇지 않으면 while문을 탈출한다.
    treeHit+= 1
    print("나무를 %d번 찍었습니다."% treeHit)
    if treeHit == 10:
        print("나무가 넘어 갑니다.")
    else:
        print("영차!")