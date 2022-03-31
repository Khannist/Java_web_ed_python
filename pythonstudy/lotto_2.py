import random

def lotto_gen():
    lotto = []
    while True:
        a = random.randint(1,45)
        if a in lotto:
            print("중복되었습니다.")
        else:
            lotto.append(a)
            if len(lotto) >= 6:
                break
    print(lotto)        

while True:
    ecq = input("로또 번호를 생성하시겠습니까? (y/n) : ")

    if ecq in ['y','Y']:
        lotto_gen()
    elif ecq in ['n','N']:
        break