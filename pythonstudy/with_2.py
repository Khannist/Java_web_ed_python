#파일 입출력

score_file = open("score.txt", "w", encoding="utf-8")
print("수학 : 0", file=score_file)
print("영어 : 50", file=score_file)
score_file.close()

score_file = open("score.txt", "a", encoding="utf-8")
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100")
score_file.close()

print(1)

score_file = open("score.txt", "r", encoding="utf-8")
print(score_file.read())
score_file.close()

print(2)

score_file = open("score.txt", "r", encoding="utf-8")
print(score_file.readline())
print(score_file.readline())
print(score_file.readline(), end="")
print(score_file.readline(), end="")
print(score_file.readline(), end="")
print(score_file.readline(), end="")
score_file.close()

print("\n3")

print()

print(4)

# 파일이 몇줄 인지 모를 때
score_file = open("score.txt", "r", encoding="utf-8")
while True:
    line = score_file.readline()
    if not line:
        break
    print(line, end="")
score_file.close()

print("\n5\n")

# list 형태로 저장
score_file = open("score.txt", "r", encoding="utf-8")
lines = score_file.readlines() # 여러줄 한꺼번에 읽어 오기
for line in lines:
    print(line, end="")

score_file.close()