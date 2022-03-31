# __init__ 생성자 : 객체가 생성될 때 자동으로 메소드가 호출되어 초기값이 설정되는 특별한 메소드이다.

# a = FourCal() a 객체 생성
# b = FourCal() b 객체

#객체를 생성과 동시에 인수값을 전달하는 방법이 없을까? 그것이 바로 생성자라고 한다.

class FourCal():
    def __init__(self, first, second):  # __init__ 객체 생성시에 초기값 설정
        self.first = first
        self.second = second
        
    def add(self):
        result = self.first + self.second
        return result
        
    def sub(self):
        result = self.first - self.second
        return result
        
    def mul(self):
        result = self.first * self.second
        return result
        
    def div(self):
        result = self.first / self.second
        return result

    def mod_c(self):
        result = self.first % self.second
        return result
    
    #객체를 생성
a = FourCal(4,2) #a 라는 객체를 생성함과 동시에 __init__ 생성자를 무조건 자동 호출하게 됨
                        # 생성자는 해당 클래스의 이름과 반드시 동일하면 생성자라고 한다.
                        
b = FourCal(3, 8) #b라는 객체를 생성함과 동시에 __init__ 생성자를 무조건 자동 호출하게 됨

print(a.add())
print(a.sub())
print(a.mul())
print(a.div())
print(a.mod_c())
print()
print(b.add())
print(b.sub())
print(b.mul())
print(b.div())
print(b.mod_c())