# 로또번호 자동 생성(단 한번)

import random

# while True:
    
#     lotto = []
#     while True:
#         a = random.randint(1, 45) # 1~45 까지의 정수를 랜덤 발생
#         if a in lotto: # in 속하는 not in 속하지 않은
#             print("중복되었습니다.")
#         else:
#             lotto.append(a)
#             if len(lotto) == 6:
#                 break
            
#     print(lotto)
    
    
# lotto_gen() 로또번호 랜덤발생해서 리스트 보관 후 출력하는 함수
# while문 y/n 여부를 결정하여 y 선택시 lotto_gen()함수를 호출하는 방식
# 시험문제

def lotto_gen():
    lotto = []
    while True:
        a = random.randint(1, 45)
        if a in lotto:
            print("중복되었습니다.")
        else:
            lotto.append(a)
            if len(lotto) == 6:
                break
    print(lotto)

c = True
while True:
    b = str(input("로또번호 자동 생성기입니다. 계속하시겠습니까> (y/n): "))
    if b in ['y', 'Y']:
        c = True
        if c:
            lotto_gen()    
    elif b in ['n', 'N']:
        break
    else:
        print("다시 입력해주세요.")
        c = False