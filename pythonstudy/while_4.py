# 커피자판기 2
# while_4.py

coffee = 10

while True: # 무한루프 => 반드시 break문이 있어야함
    money = int(input("돈을 넣어주세요 : "))
    if money == 300:
        print("커피를 줍니다.")
        coffee -= 1
        print("커피가 %d잔 남았습니다."% coffee)
    elif money > 300:
        print("커피를 줍니다.")
        print("거스름돈 %d를 줍니다."% (money - 300))
        coffee -= 1
        print("커피가 %d잔 남았습니다."% coffee)
    else:
        print("돈을 다시 돌려주고 커피를 주지 않습니다.")
        print("커피가 %d잔 남았습니다."% coffee)
    
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break