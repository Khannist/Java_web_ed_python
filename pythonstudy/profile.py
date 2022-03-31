# def profile(name, age, address):
#     print("나의 이름은 %s이고, 나이는 %d이고, 주소는 %s입니다."%(name,age,address))
    
def profile(name, age, address):
    print("나의 이름은 {0}이고, 나이는 {1}이고, 주소는 {2}입니다.".format(name,age,address))
    
    
    
name = input("이름을 입력하세요>> ")
age = int(input("나이를 입력하세요>> "))
address = input("주소를 입력하세요>> ")

profile(name, age, address)
