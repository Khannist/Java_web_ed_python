from re import S


prompt = """
1. Add
2. Del
3. List
4. Quit

Enter number : """

number = 0
while number != 4:
    print(prompt)
    number = int(input()) #input() 임의의 수 키보드 입력
