#menu

# Americano 가격 3000원
# Ice Americano 가격 3500원
# Cappuccino 가격 4000원
# cafeLatte 가격 4500원
# Espresso 가격 3600원
# 위의 메뉴중 하나를 선택해주세요: Americano
# Americano는 3000원 입니다. 결제를 부탁드립니다.
# 만약 메뉴에 없는 종목이면 미안합니다. ooo는 메뉴에 없습니다.
#print('{:<15} 가격 : {}원'.format)
menu = {'Americano':'3000','Ice Americano':'3500','Cappuccino':'4000'
        ,'CafeLatte':'4500','Espresso':'3600'}

while True:
    for i in menu:
        # print('{0}  가격 : {1}원'.format(i,menu.get(i)))
        # print('{:<15}'.format(i),end='')
        # print('{:<4}'.format('가격 :'),end='')
        # print('{:<5}'.format(menu.get(i),'원'))
        print('{:<15} 가격 : {}원'.format(i,menu[i]))
        if i == 'Espresso':
            break
    sel = input("\n위의 메뉴중 하나를 선택해주세요: ")   
    if sel in menu:
        print(f"주문하신 {sel}는 {menu.get(sel)}원 입니다. 결제를 부탁드립니다.")
    else:
        print(f"미안합니다. {sel}는 메뉴에 없습니다.")
