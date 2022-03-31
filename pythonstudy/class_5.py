#Student 클래스를 선언

class Student: #클래스는 첫 글자 무조건 대문자, 합성 단어 각각 대문자 FourCal 클린코드 = 가독성 높히기 위함
    count = 0 #클래스 변수 초기화
    
    def __init__(self, name, korean, math, english, science): #매개변수
        self.name = name # self.name => 멤버변수, name => 매개변수
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
        
    #클래스변수 카운트 설정
        Student.count += 1
        print(f'{Student.count}번째 학생이 생성되었습니다.')    
    
    def get_sum(self):  #합계를 구한다.
        return self.korean + self.math + self.english + self.science

    def get_avarage(self): #평균을 구한다.
        return self.get_sum() / 4
        
    def __str__(self):
        return "{}\t{}\t{}".format(self.name, self.get_sum(), self.get_avarage())        
        
#학생 list 선언
students = [   #[] 리스트, () 튜플, {}set(집합), 딕셔너리
    Student("윤인성",87,98,88,95),
    Student("옥수수",77,87,67,71),
    Student("수염차",82,21,74,54),
    Student("븨라인",77,14,89,44),
    Student("가나초",95,9,99,23),
    Student("코올릿",75,5,45,80)

]
# 학생 한명씩 출력

print("이름","총점","평균",sep="\t")
for student in students:
    print(str(student))