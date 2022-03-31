from random import *
# 마린 3기, 탱크 2기, 레이스 1기를 생성하여 전군 1시 방향으로 공격개시!

# 일반 유닛
class Unit:
    def __init__(self,name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} 유닛이 생성되었습니다.\n".format(self.name))
        
    def move(self, location):
        print("{0} : {1} 방향으로 이동합니다 [속도{2}]\n".format(self.name, location, self.speed))
        
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 체력이 {1} 남았습니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.\n".format(self.name))
        else:
            print()
            
# 공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage
        
    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력{2}]\n".format(self.name, location, self.damage))
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
        
    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도{2}]\n".format(name, location, self.flying_speed))
        
# 공중 공격 유닛 클래스

class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) # speed = 지상유닛의 스피드
        Flyable.__init__(self, flying_speed) # flying_speed = 공중유닛의 스피드
        
    def move(self, location):
        self.fly(self.name, location)


#레이스
class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
        self.clocked = False # 클로킹 모드 (해제 상태)

    def clocking(self):
        if self.clocked == True:
            print("{0} : 클로킹 모드 해제합니다.\n".format(self.name))
            self.clocked = True

class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 1, 5)
    #스팀팩 : 일정 시간 동안 이동 및 공격 속도를 증가, 체력 10 감소

    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{0} : 스팀팩을 사용합니다. (hp 10 감소)\n".format(self.name))
        else:
            print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다.\n".format(self.name))
            
class Tank(AttackUnit):
    # 시즈모드 : 탱크를 지상에 고정시켜, 더 높은 파워로 공격 가능 모드, 이동은 불가!
    seize_developed = False
    
    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 1, 35)
        
    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return
        
        # 현재 시즈모드가 아닐 때 -> 시즈모드
        if self.seize_developed == False:
            print("{0} : 시즈모드로 전환합니다\n".format(self.name))
            self.damage *= 2
            self.set_seize_mode = True
            
        else: # 현재 시즈모드 일 때 -> 시즈모드 해제
            print("{0} : 시즈모드를 해제합니다.\n".format(self.name))
            self.damage /= 2
            self.set_seize_mode = False
            
    
def game_start():
    print("[알림] 새로운 게임을 시작합니다.")
    
def game_over():
    print("Player : gg")
    print("[Player] 님이 퇴장하셨습니다.")

#실제 게임 시작

game_start()

marine1 = Marine()
marine2 = Marine()
marine3 = Marine()

tank1 = Tank()
tank2 = Tank()

wraith1 = Wraith()

attack_units = []
attack_units.append(marine1)
attack_units.append(marine2)
attack_units.append(marine3)
attack_units.append(tank1)
attack_units.append(tank2)
attack_units.append(wraith1)

for unit in attack_units:
    unit.move("1시")

# 탱크 시즈모드 개발
Tank.seize_developed = True
print("[알림] 탱크 시즈 모드 개발이 완료되었습니다.\n")

#공격 모드 준비(마린: 스팀팩, 탱크: 시즈모드, 레이스: 클로킹)

for unit in attack_units:
    if isinstance(unit, Marine):
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    elif isinstance(unit, Wraith):
        unit.clocking()
        
#전군 공격
for unit in attack_units:
    unit.attack("1시")
    
a = 1
temp = ""
for unit in attack_units:
    if  temp == unit.name:
        a += 1
    else:
        a = 1
    while True:
        if unit.hp > 0:
            print(unit.name, a)
            unit.damaged(randint(22, 100))
        else:
            break
    temp = unit.name
        
game_over()