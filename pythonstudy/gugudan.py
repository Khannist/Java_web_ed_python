# 구구단 실행하기

# def dan():
#     while True:
#         n = int(input("출력할 단 입력(종료: 0): " ))
#         if n == 0:
#             break
#         else:
#             for i in range(1, 10):
#                 print("{0} x {1} = {2}".format(n, i, n*i))
#         print()
                
# dan()

# 리스트 입력받아서 차례대로 출력

x = 1
list = []
while x!=0:
    x = int(input("출력할 단을 입력하세요 : "))
    if x!= 0:
        list.append(x)
        
print("출력할 구구단: ",list)
for i in list:
    y = 0
    while y <= 8:
        y = y+1
        print(i,"x",y,"=",i*y)
    print()
