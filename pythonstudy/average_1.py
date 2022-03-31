# A 학급에 총 10명의 학생이 있다.
# 이 학생들의 중간고사 점수는 다음과 같다.
# [70, 60, 55, 75, 95, 90, 80, 85, 100, 81]

#for문을 이용하여 A학급의 평균점수를 출력하시오.

# a = [70, 60, 55, 75, 95, 90, 80, 85, 100, 75]
# average = 0
# total = 0

# for score in a:
#     total += score
    
# average = total / len(a)   
# print("A학급의 평균점수는 %.2f점 입니다."%average)
from xmlrpc.client import boolean


while True:
    
    def stars(i, j, k, h):
        while True:
            print(" "*j,end="")
            print("*"*i)
            k += 1
            if k < (h/2):
                j -= 1
                i += 2
            elif k >= (h/2)-1:
                j += 1
                i -= 2
                
            if k >= h+1:
                break

    i = int(input("i값 = "))
    j = int(input("j값 = "))
    k = int(input("k값 = "))
    h = int(input("h값 = "))

    stars(i,j,k,h)
    
    trft = input("계속 하시겠습니까? y/n >>")
    if(trft == 'y' or trft == 'Y'):
        continue
    elif(trft == 'n' or trft == 'N'):
        break
