class FourCal:  #FourCal 상위클래스, 슈퍼클래스, 부모클래스
    # 상속 : 상위클래스(부모클래스)의 속성, 생성자, 메소드 등을 물려받아 하위클래스(자식클래스)
    # 에서 사용할 수 있는 기능이다.
    def __init__(self,first,second):
        self.first = first
        self.second = second
        
    def add(self):
        return self.first + self.second 
        
    def sub(self):
        return self.first - self.second 
        
    def mul(self):
        return self.first * self.second 

    def div(self):
        return self.first / self.second 

    # def mod_c(self):
    #     return self.first % self.second 
    
class MoreForeCal(FourCal):
    def div(self):    #메소드 오버라이딩: 상위클래스의 특정 메소드를 하위클래스에서 재정의한다.
                        # 동일한 메소드 이름으로 작성한다. 그리고 그 내용만 바꾼다. 덮어쓰기기능이다.
        if self.second == 0:
            return 0
        else:
            return self.first / self.second


# a1 = FourCal(4,2)  기존 클래스방식, 생성자 호출==> __init__ 생성자에 가서 초깃값 부여
a2 = MoreForeCal(0,4)
# a = FourCal(0,4)

print(a2.add())
print(a2.sub())
print(a2.mul())
print(a2.div()) # 메소드 오바라이딩 하면 부모클래스 클래스의 div()가 아닌
                # 자식클래스의 div() 메소드로 호출한다.