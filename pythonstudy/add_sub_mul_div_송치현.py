import random as r

def addition():    
    Lran = r.randint(1,20)
    Rran = r.randint(1,9)
    print(f"{Lran} + {Rran} = ",end="")
    ans = int(input())
    check(Lran + Rran, ans)
    
def subtraction():
    Lran = r.randint(1,20)
    Rran = r.randint(1,9)
    print(f"{Lran} - {Rran} = ",end="")
    ans = int(input())
    check(Lran- Rran, ans)
    
def multiply():
    Lran = r.randint(1,20)
    Rran = r.randint(1,9)
    print(f"{Lran} * {Rran} = ",end="")
    ans = int(input())
    check(Lran * Rran, ans)
    
def division():
    Lran = r.randint(1,20)
    Rran = r.randint(1,9)
    print(f"{Lran} / {Rran} = ",end="")
    ans = int(input())
    check(int(Lran / Rran), ans)

def check(check, ans):
    if check == ans:
        print("정답입니다.")
    else:
        print(f"틀렸습니다. 정답은 {check} 입니다.")
    
def main():
    while True:
        print("\n1) Addition\n2) Subtraction\n3) Multiply\n4) Division\n")
        cho = int(input("Enter 1 ~ 4 : "))
        if cho == 1:
            addition()
        elif cho == 2:
            subtraction()
        elif cho == 3:
            multiply()
        elif cho == 4:
            division()
        else:
            print("유효하지 않습니다. 다시 입력해주세요.")

    
    
    
main()