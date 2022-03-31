


while True:
    tmp = int(input("단을 입력하세요 : "))

    if tmp <= 0:
        break
    else:
        for i in range(1, 10):
            print("%d x %d = %d"%(tmp, i, tmp*i))