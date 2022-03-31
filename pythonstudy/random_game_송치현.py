# # 숫자를 맞춰보세요. (1-100) : 4
# # 숙자가 너무 큽니다.
# # 숫자를 맞춰보세요. (1-100) : 3
# # 정답입니다. 입력한 숫자는 3입니다.
# # 게임스코어는 [2, 3, 5, 7, 3]입니다.
# # 평균적으로 4회만에 맞추셨습니다.

# # random 수 하나를 입력받아 사용자가 몇회에 맞추는가를
# # 총 5게임으로 진행하되 1게임당 맞춘 횟수를 score 리스트에
# # 저장후 최종적으로 5게임이 끝나면
# # 게임스코어는 입니다.
# # 평균적으로 4회만에 맞추셧습니다.

# # get_num(): 사용자 숫자 입력하는 함수

# # game(): 컴퓨터 랜덤숫자와 사용자 수 비교 처리문
# # 숫자가 너무 큽니다.
# # 숫자가 너무 작습니다.
# # counter : 1게임당 맞추는 횟수를 누적하여, score 리스트에 저장 
# # 1회차 게임 --------------------------------
# # 숫자를 맞춰보세요. (1-100) : 


# import random as r


# score = []
# counter = 0
# ctr = 1

# while True:
#     print(f'{ctr}회차 게임 ','-'*30)
#     b = r.randint(1,5)
#     while True:
#         a = int(input("숫자를 맞춰보세요.(1-100) : "))
            
#         if a > b:
#             print('숫자가 너무 큽니다.')
#         elif a < b:
#             print('숫자가 너무 작습니다.')
#         else:
#             print(f'정답입니다. 입력한 숫자는 {a}입니다.')
#             break
#         counter += 1
    
#     score.append(counter)
#     ctr += 1
    
#     if ctr == 6:
#         break

  
# print(f'게임스코어는 {score} 입니다.')
# print(f'평균적으로 {sum(score)/len(score)}회만에 맞추셧습니다.')

import random as r

def com_rand():
    return r.randint(1,100)

def get_num():
    return int(input("숫자를 맞춰보세요.(1-100) : "))

def game(b):
    counter = 1
    while True:
        n = get_num()
        if n > b:
                print('숫자가 너무 큽니다.')
        elif n < b:
                print('숫자가 너무 작습니다.')
        elif n == b:
            print(f'정답입니다. 입력한 숫자는 {n}입니다.')
            return counter        
        else:
            print("오류")
        counter += 1
    
score = []


for i in range(1,6):
    print(f'{i}회차 게임 ','-'*30)
    num = com_rand()
    
    score.append(game(num))

print(f'게임스코어는 {score} 입니다.')
print('\n평균적으로 %.f회만에 맞추셧습니다.'%(sum(score)/len(score)))