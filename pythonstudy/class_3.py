from functools import total_ordering


class Person:
    total_count = 0 #클래스 변수(=속성, 데이터, 필드)

    def __init__(self, name, age):
        self.name = name
        self.age = age
        # total_count += 1 # 클래스변수에 접근할때에는 반드시 클래스명, 클래스변수
        Person.total_count += 1

    def introduce(self):
        print(f'나의 이름은 {self.name}이고, 나이는 {self.age}살 입니다.')

p1 = Person('송치현', 25)
p2 = Person('옥수수', 18)
p3 = Person('수염차', 32)
p4 = Person('가나초', 41)
p5 = Person('콜릿롯', 27)
p6 = Person('데광동', 14)

# p1~p6 인조로봇 생성
print("person클래스로 부터 객체가 생성되고 있습니다.")
p1.introduce()
p2.introduce()
p3.introduce()
p4.introduce()
p5.introduce()
p6.introduce()
print(Person.total_count)
#각객체를출력

#우리반은 모두 6명 입니다.
#우리 6명의 클래스는 모두 Person입니다.

print(f'우리반은 모두 {Person.total_count}명 입니다.')
print(f"우리 {Person.total_count}명의 클래스는 모두 {Person.__name__}입니다.")