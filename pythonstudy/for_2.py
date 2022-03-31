# for_2.py

add = 0
for i in range(1, 58,2):
    print("%d + %d = %d" % (add,i,add+i))
    add += i
    
print("최종값 = ", add)