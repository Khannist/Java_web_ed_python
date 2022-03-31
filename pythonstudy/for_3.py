# 구구단
# for_3.py

# for i in range(2, 10):
#     print("%d단"%i)
#     for j in range(1, 10):
#         print("%d x %d = %d"%(i,j,i*j))
#         # print(i*j, end=" ")
#     print("")

# for i in range(2, 10):
#     for j in range(1, 10):
#         print(i*j, end = " ")
#     print('')
    
# a = [1,2,3,4]

# result = []
# for num in a:
#     result.append(num*3)
    
# print(result)

# result = [x*y for x in range(2,10)
#             for y in range(1,10)]

# print(result)


# 1부터 1000까지의 수중에서 3의 배수의 합을 구해보자
# 3의 배수이면서 5의 배수인 수를 누적하고 출력
# result = 0
# i = 1
          
# while i <= 100:
    
#     if(i % 3) == 0:
#         if(i % 5) == 0:
#             result += i
            
#     i += 1

# while i <= 100:
    
#     if(i % 3 == 0) and (i % 5 == 0):
#         result += i
#         print(i)
#     i += 1
      
# print(result)




# i = 0
# while True:
#     i += 1
#     if i > 7:
#         break
#     print("*"*i)

i = 1
j = 3
k = 0
while True:
    print(" "*j,end="")
    print("*"*i)
    k += 1
    if k < 4:
        j -= 1
        i += 2
    elif k >= 3:
        j += 1
        i -= 2
        
    if k >= 7:
        break


# i = 6
# while True:
#     i -= 1
#     if i >= 0:
#         break
#     print("*"*i)

#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *