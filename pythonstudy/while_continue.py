# # while_continue.py

# a = 0
# while a < 10:
#     a += 1
#     if a % 2 == 0:
#       continue # continue 를 만나면 다음 한 줄 처리를 skip한다.
#     print(a)


# 1 ~ 10까지의 짝수의 합
i,sum = 0,0

while i < 10:
    i += 1
    if i % 2 == 1: #i 값이 홀수 일때는 continue를 만나서
        continue    #그다음 문장인 sum을 누적을 하지 않고,
    sum += i        #i 값이 짝수 일때는 sum에 누적시킨다.
print(sum)