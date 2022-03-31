import random

# def low_high_range():
#     low = int(input('낮은 숫자를 입력하세요:'))
#     high = int(input('높은 숫자를 입력하세요:'))
#     num = random.randint(low,high)
#     return num

# def check(ask, comp_num):
#     if(ask == comp_num):
#         print('정확합니다. 게임에 승리하였습니다.')
#         return False
#     else:
#         if(ask > comp_num):
#             print('\n너무 높은 숫자입니다.')
#         elif(ask < comp_num):
#             print('\n너무 낮은 숫자입니다.')
#     return True
            
# def user_ask():
#     return int(input("당신이 생각하는 숫자는 무엇인가요?...: "))

# def main():
#     comp_num = low_high_range()
#     state = True
#     while state:
#         ask = user_ask()
#         state = check(ask, comp_num)
        

# main()


def low_high_range():
    low = int(input('낮은 숫자를 입력하세요:'))
    high = int(input('높은 숫자를 입력하세요:'))
    num = random.randint(low,high)
    #print(num)
    return num

def user_ask():
    ask = int(input("당신이 생각하는 숫자는 무엇인가요?...: "))
    return ask

def check(ask, comp_num):
    if(ask == comp_num):
        return True
    else:
        return False
        
            
def main():
    comp_num = low_high_range()
    state = True
    while state:
        user_ask_int = user_ask()
        if check(user_ask_int, comp_num):
            state = False
            print('정확합니다. 게임에 승리하였습니다.')
        else:
            if user_ask_int < comp_num:
                print('\n너무 낮은 숫자입니다.')
            elif user_ask_int > comp_num:
                print('\n너무 높은 숫자입니다.')
        

main()