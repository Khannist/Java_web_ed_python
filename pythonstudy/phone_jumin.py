from sqlite3 import DataError
from unittest import result
import re

# data = '''
# park 950101-1010101
# kim  960202-2020202
# lee  901218-2456254
# '''

# result = []
# for line in data.split('\n'):
#     print('line = ',line)
#     word_result = []
#     for word in line.split(' '):
#         print('word1 = ', word)
#         if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit():
#             word = word[:6] + '-' + '*******'
#             print('word3 = ',word)
#         print('world_result1 = ',word_result)
#         word_result.append(word)
#         print('world_result2 = ',word_result)
#     print('result1 = ', result)
#     result.append(' '.join(word_result))
#     print('result2 = ', result)
    
# print('result3 = ', result)
# print('\n'.join(result))

# data = '''
# park 800905-1049118
# kim  980905-1059119
# lee  901218-2456254
# '''

# pat = re.compile("(\d{6})[-]\d{7}")
# print(pat.sub("\g<1>-*******",data))

# pat = re.compile("\d{6}[-](\d{7})")
# print(pat.sub("******-\g<1>", data))

s = '''
park 010-9999-9988
kim  010-9909-7789
lee  010-8789-7796
'''


pat = re.compile("(\d{3}[-]\d{4})[-]\d{4}")
print(pat.sub("\g<1>-####", s))

pat = re.compile("(\d{3})[-]\d{4}[-](\d{4})")
print(pat.sub("\g<1>-####-\g<2>", s))

pat = re.compile("(\d{3})[-](\d{4})[-](\d{4})")
print(pat.sub("####-\g<2>-\g<3>", s))