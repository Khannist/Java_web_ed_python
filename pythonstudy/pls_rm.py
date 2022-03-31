#랜덤 수 a와 b를 입력받아서
#출력형태처럼 정답이면 "정답입니다. -- 축하합니다!"
#오답이면 "틀렸습니다. 정답은 000 입니다."

import random as r

while True:
    a = r.randint(10,99)
    b = r.randint(100,999)
    print(f"   {a}\n+ {b}\n{'-'*5}")
    c = int(input())

    if c == (a+b):
        print("정답입니다. -- 축하합니다!")
    else:
        print(f'틀렸습니다. 정답은 {a+b} 입니다.')