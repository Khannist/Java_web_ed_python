# local : 지역변수
# global : 전역변수

from math import radians


def circle_area():
    area = 3.14 * radius ** 2   #지역변수 area, 지역변수는 함수 내에서만 사용되고 함수 밖으로 나가면 소멸된다.
    return area

area = "옥수"
radius = float(input("반지름을 입력하세요>> "))
print("원의 넓이: ", circle_area())
print(area)

def circle_area():
    global area
    area = 3.14 * radius ** 2
    return area

area = 0

radius = float(input("반지름을 입력하세요>> "))
print("원의 넓이: ", circle_area())
print(area)