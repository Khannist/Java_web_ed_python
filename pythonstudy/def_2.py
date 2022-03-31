from unittest import result


# def add_many(*args):
#     result = 0
#     for i in args:
#         result += i
#     return result

# result = add_many(1,2,3,4,5,6,7,8,9,10)
# print(result)
  
# def add_mul(choice, *args):
#     if choice == "add":
#         result = 0
#         for i in args:
#             result += i
#     elif choice == 'mul':
#         result = 1
#         for i in args:
#             result *= i
#     return result



# result = add_mul("add",1,2,3,4,5,6)
# print(result)

# result = add_mul("mul",1,2,3,4,5,6)
# print(result)

# def say_nick(nick):
#     if nick == '바보':
#         return print("바보, 바보")
#     print("나의 별명은 %s입니다."%nick)
    
    
# say_nick('야호')
# say_nick('바보')

def say_myself(name, old, man=True):
    print("나의 이름은 %s입니다."%name)
    print("나이는 %d입니다."%old)
    if man == True:
        print("남자입니다.")
    else:
        print("여자입니다.")


say_myself("송치현", 25, 1)
say_myself("옥수수", 36, 0)
say_myself("수염차", 500, 1)