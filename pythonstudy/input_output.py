# """ 여러줄 주석처리 """~~~~"""
print("Python", "Java", "JavaScript") # Python Java JavaScript
print("Python", "Java", "JavaScript", sep="") # PythonJavaJavaScript
print("Python", "Java", "JavaScript", sep=" vs ") # Python vs Java vs JavaScript
print("Python", "Java", "JavaScript", sep=",") # Python,Java,JavaScript? 
print("\n무엇이 더 재미있을까요?") # end="" 다음 줄의 print문을 이어붙이는 기능

scores = {"수학" : 0, "영어" : 50, "코딩" : 100}  # 딕셔너리
for subject, score in scores.items():
  # print(subject, score)
    print(subject.ljust(3), str(score).rjust(4), sep=":") # 정형화된 포맷
                 # ljust 왼쪽 정렬, rjust 오른쪽 정렬, str : 숫자를 문자형 변환
# 은행 대기순번표
# 001, 002, 003, .....

for num in range(1, 21): # 1~20까지 반복 실행
    print("대기번호 : " + str(num).zfill(3))  # zfill 빈자리는 0으로 채워짐

answer1 = input("첫번째 아무 값이나 입력하세요 : ")
print("입력한 값은 " + answer1 + "입니다.")
print(type(answer1))

answer2 = int(input("두번째 아무 값이나 입력하세요 : "))
# print("입력한 값은 " + answer2 + "입니다.")  # 스트링과 숫자형은 연결연산자 사용 불가
print(type(answer2)) # 따라서 수치데이터 연산에는 무조건 int 형변환을 해줘야 함.
# 숫자 타입변환은 int, 문자 타입변환은 str

# 10자리 확보하고, 빈자리는 빈공간으로 두고, 오른쪽 정렬하라.
print("{0:>10}".format(500)) 

# 양수일 땐 +로 표시, 음수일 땐 -로 표시
print("{0:>+10}".format(500))
print("{0:>+10}".format(-500))

# 왼쪽 정렬하고, 나머지는 _로 채움
print("{0:_<+10}".format(500))
print("{0:_>10}".format(500))

# 3자리마다 콤마
print("{0:,}".format(1000000000))
# 3자리마다 콤마하고, 부호(+,-)도 붙이고
print("{0:-,}".format(-1000000))

# 빈자리는 ^ 로 채워주기, 왼쪽 정렬, 세자리 콤마
print("{0:^<+20,}".format(1000000))

# 소수점 출력
print("{0:f}".format(5/3))

# 소수점 특정 자리수 까지만 표시(소수점 셋짜자리에서 반올림)
print("{0:.2f}".format(5/3))