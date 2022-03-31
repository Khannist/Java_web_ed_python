from calendar import month
import datetime

now = datetime.datetime.now()

print("{}년 {}월 {}일 {}시 {}분 {}초".format(
    now.year,   #년
    now.month,  #월
    now.day,    #일
    now.hour,   #시
    now.minute, #분
    now.second  #초
))
print("년 : {:>6}년".format(now.year))
print("월 : {:>6}월".format(now.month))
print("일 : {:>6}일".format(now.day))
print("시 : {:>6}시".format(now.hour))
print("분 : {:>6}분".format(now.minute))
print("초 : {:>6}초".format(now.second))


# 현재 시각은 {}시로 오전입니다!
# 현재 시각은 {}시로 오후입니다!
# 이번달은 {}월로 봄입니다!
# 이번달은 {}월로 여름입니다!
# 이번달은 {}월로 가을입니다!
# 이번달은 {}월로 겨울입니다!

# if now.hour > 12:
#     print("현재 시각은 {}시로 오후입니다!".format(now.hour))
# else:
#     print("현재 시각은 {}시로 오전입니다!".format(now.hour))
    
# if now.month in [3,4,5]:
#     print("이번달은 {}월로 봄입니다!".format(now.month))
# elif now.month in [6,7,8]:
#     print("이번달은 {}월로 여름입니다!".format(now.month))
# elif now.month in [9,10,11]:
#     print("이번달은 {}월로 가을입니다!".format(now.month))
# else:
#     print("이번달은 {}월로 겨울입니다!".format(now.month))