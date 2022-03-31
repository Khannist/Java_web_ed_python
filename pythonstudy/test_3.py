import re

# 파이썬에서는 문자열 '이진수','이진수',"""이진수""",'''이진수'''
data = """
park 800905-1049118
kim  980905-1059119
lee  901218-2456254
""" #여러준 문자열은 반드시 ''',""" 묶어준다.

pat = re.compile("(\d{6})[-](\d{7})")
print(pat.sub("\g<1>-"+"#"*7,data))

pat = re.compile("\d{6}[-](\d{7})")
print(pat.sub("*"*6+"-\g<1>", data))
print(pat)

s = """
park 010-9999-9988
kim  010-9909-7789
lee  010-8789-7796
"""

at = re.compile("(\d{3}[-]\d{4})[-]\d{4}")
result = at.sub("\g<1>-****", s)
print(result)

at = re.compile("(\d{3})[-]\d{4}[-](\d{4})")
result = at.sub("\g<1>-****-\g<2>", s)
print(result)

at = re.compile("\d{3}[-](\d{4}[-]\d{4})")
result = at.sub("***-\g<1>", s)
print(result)

