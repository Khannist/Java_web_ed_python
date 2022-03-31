import re

data = """
1110-12-27-4428
1157-45-33-9875
3568-98-01-8854
"""

pat = re.compile("(\d{4})[-]\d{2}[-]\d{2}[-](\d{4})")
print(pat.sub("\g<1>-**-**-\g<2>", data))

pat = re.compile("\d{4}[-](\d{2}[-]\d{2})[-]\d{4}")
print(pat.sub("****-\g<1>-****", data))

pat = re.compile("(\d{4}[-]\d{2}[-]\d{2})[-]\d{4}")
print(pat.sub("\g<1>-****", data))

pat = re.compile("(\d{1})\d{3}[-]\d{2}[-]\d{2}[-](\d{4})")
print(pat.sub("\g<1>***-**-**-\g<2>", data))
