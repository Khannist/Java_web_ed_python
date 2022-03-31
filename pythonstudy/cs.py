from re import S


# def cs(n):
#     s = 0
#     for num in range(2, n, 2):
#         s += num  
#     return s

# print(cs(101))

# class CharClass:
#     a = ['Seoul', 'Kyeongi','Inchon','Daejeon','Daegu','Pusan']

# myVar,myVar02 = CharClass(), CharClass()

# str01,str02 = '',' '

# for i in myVar.a:
#     str01 = str01 + i[0]
# for j in myVar02.a:
#     str02 = str02 + j[-1]

# print(str01)
# print(str02)

# lol = [[1,2,3],[4,5],[6,7,8,9]]
# print(lol[0])
# print(lol[2][1])
# for sub in lol:
#     for item in sub:
#         print(item, end=' ')
#     print()
# for sub in lol:
#     for item in sub:
#         print(item, end='')
#     print()
# for sub in lol:
#     for item in sub:
#         print(item, end='')
#     print()
# for sub in lol:
#     for item in sub:
#         print(item, end='#')
#     print()

asia = {'한국', '중국', '일본'}
asia.add('베트남')
asia.add('중국')
asia.remove('일본')
asia.update({'한국','홍콩','태국'})
print(asia)