# 클래스와 메소드를 이용한 스타크래프트2
# class_def_starcraft_2.py

# 클래스이름 : Unit

class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print(f'{self.name} 유닛이 생성되었습니다.')
        print(f'{self.name}: 체력 {self.hp} 공격력 {self.damage}\n')


marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank1 = Unit("탱크", 150, 35)
tank2 = Unit("탱크", 150, 35)
tank3 = Unit("탱크", 150, 35)

# 레이스 : 공중 유닛, 비행기, 클로킹(성대방에게 보이지 않음)
wraith1 = Unit("레이스", 80, 5)

print(f"유닛 이름: {wraith1.name}, 공격력 : {wraith1.damage}\n")

# 마인드컨트롤 : 적군을 아군으로
wraith2 = Unit("빼앗은 레이스", 80, 5)

print(f"유닛 이름: {wraith2.name}, 공격력 : {wraith2.damage}\n")
wraith2.clocking = True

if wraith2.clocking == True:
    print(f"{wraith2.name}는 현재 클로킹 상태입니다.\n")