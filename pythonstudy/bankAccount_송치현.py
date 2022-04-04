Bexit = True
Sid = "Python"
Ipwd = 1234
Account = 0

def menu_cho(menu_input):
    if menu_input == 1:
        mny_in()
    elif menu_input == 2:
        mny_out()
    elif menu_input == 3:
        print(f"잔액은 {Account}원 입니다.")
    elif menu_input == 4:
        print("종료하겠습니다.")
        return False
    return True

def mny_in():
    global Account
    IAccount = int(input("입금할 금액을 입력하세요 : "))
    Account += IAccount
    print(f"잔액은 {Account}원 입니다.")

def mny_out():
    global Account
    OAccount = int(input("출금할 금액을 입력하세요 : "))
    if (Account - OAccount) < 0:
        print(f"금액이 부족합니다.[남은 잔액: {Account}]")
    else:
        Account -= OAccount
        print(f"잔액은 {Account}원 입니다")
         
    
def login():
    while True:
        ISid = input("아이디를 입력하세요 : ")
        if ISid == Sid:
            IIpwd = int(input("비밀번호를 입력하세요 : "))
            if IIpwd == Ipwd:
                print("로그인이 되었습니다.. ")
                break
            else:
                print("잘못 입력하셨습니다.")
        else:
            print("잘못 입력하셨습니다.")



login()

while Bexit:
    print("\n"+"="*30)   
    print("1. 입금\n2. 출금\n3. 잔액조회\n4. 종료")
    print("="*30)
    menu_input = int(input("\n원하시는 메뉴의 번호를 입력하세요 : "))
    Bexit = menu_cho(menu_input)