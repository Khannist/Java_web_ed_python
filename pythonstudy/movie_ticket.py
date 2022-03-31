# 영화 예매하기
# 해당되는 리스트(movies)의 목록 영화명을 선택하면,
# 관람인원을 선택하게 하고,
# 할인권이 있으면, y를 선택하고 없으면, 할인쿠폰 코드를 입력하면
# 할인 금액이 적용된 청구금액을 출력해준다.

from tabnanny import check


movies = ["스파이더맨", "아바타2", "기생충", "타이타닉", "클래식"]
print()
bkli = "=" * 10
print(bkli,"영화 목록",bkli)

for item in movies:
    print(item)
    
print(bkli,"영화 목록",bkli,"\n")
choice = input("예매하실 영화명을 입력하세요. : ")

while choice not in movies:
    print("예매할 수 없는 영화 입니다.")
    choice = input("예매하실 영화명을 입력하세요. : ")
print("예매하실 영화를 선택해주세요 : ",choice," 영화를 선택 하셨습니다.\n")

check = False

while not check:
    people = int(input("관람하실 인원을 입력하세요 : "))
    
    if people < 1:
        print("관람 인원 수를 한명 이상 입력해주세요.\n")
    else:
        print("관람 인원 수는 %d 명 이상입니다.\n"%people)
        check = True

coupon_dic = {"WELCOME":1000,"VALENTINE":2000,"CHRISTMAS":3000,"EVENTDAY":4000}
process = True
usage = input("할인권을 사용하시려면 y, 금액 확인으로 넘어가시려면 n을 입력해주세요 : ")
while process:
    if usage in ['y', 'Y']:
        coupon = input("쿠폰 코드를 입력해주세요 : ")
        if coupon in coupon_dic:
            sale = coupon_dic[coupon]
            print("%d원 할인 됩니다.\n"% sale)
            break
        else:
            print("존재하지 않는 할인권입니다.\n")
    elif usage in ['n', 'N']:
        sale = 0
        print("할인권을 사용하지 않았습니다.\n")
        break
    else:
        usage = input("잘못된 쿠폰 입력입니다. 다시 입력해주세요 : ")        
        
origin_price = 12000
sale_price = sale
total_price = (origin_price - sale_price) * people

print()
print("예매 상세 내역>")
print(bkli*3)
print("영화 제목 : {0}\n관람 인원 : {1} 명\n관람 금액 : {2}원\n할인 금액 : {3}원"\
    .format(choice, people, origin_price, sale_price))
print("-"*30)
print("청구 금액 %d원"% total_price)
print(bkli*3)