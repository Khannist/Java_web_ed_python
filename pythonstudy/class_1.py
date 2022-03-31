from unittest import result


class FourCal():
    def setdata(self, first, second):
        self.first = first
        self.second = second
        
    def add(self):
        result = self.first + self.second
        return result
    
    def mul(self):
        result = self.first * self.second
        return result
    
    def div(self):
        result = self.first / self.second
        return result
    
    def sub(self):
        result = self.first - self.second
        return result
    
    def mod_c(self):
        result = self.first % self.second
        return result
    
# 클래스를 정의했으면 객체를 생성한다. ==> 인스턴스화

a = FourCal() # FourCal 클래스의 인스턴스
a.setdata(4, 2)
print("4 + 2 = {0}".format(a.add()))
print("4 - 2 = {0}".format(a.sub()))
print("4 * 2 = {0}".format(a.mul()))
print("4 / 2 = {0}".format(a.div()))
print("4 % 2 = {0}".format(a.mod_c()))
