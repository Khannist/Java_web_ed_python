# 클래스 + 상속을 이용한 스타크래프트3
# class_inheritance_starcraft_3.py
# 상속: 단일상속(하나로부터 물려받는것), 다중상속(두개 이상의 상위클래스로부터 물려 받는것)

# 일반 유닛
class Unit: # 상위 클래스
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        
# 공격 유닛
class AttackUnit(Unit): # 하위 클래스
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)
        self.damage = damage
    
    def attack(self, location):
        print(f"{self.name} : {location} 방향으로 적군을 공격합니다. [공격력 {self.damage}]\n")
        
    def damaged(self, damage):
        print(f"{self.name} : {damage} 데미지를 입었습니다.")
        self.hp -= damage
        print(f'{self.name} : 현재 체력은 {self.hp} 입니다.')
        if self.hp <= 0:
            print(f"{self.name} : 파괴되었습니다.")

firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")
firebat1.damaged(125)
# firebat1.damaged(25)