# 커피자판기
# coffee_break.py

coffee = int(input("커피 개수를 입력하세요>> "))
money = int(input("충전금액을 입력하세요>> "))

while money and coffee:
    print("돈을 넣습니다.")
    coffee -= 1
    money -= 30
    print("남은 커피의 양은 %d개 입니다."% coffee)
    print("남은 돈은 %d원 입니다."% money)
    
    if coffee == 0:
        print("커피가 모두 소진되었습니다.\n판매중지!!!")
        break
    elif money < 30:
        print("잔액이 부족합니다.\n판매중지!!!")
        break 