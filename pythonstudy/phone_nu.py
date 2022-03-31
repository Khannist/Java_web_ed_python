#출력폼
#전화번호 저장, 전체보기
#전체보기(0),저장(1),삭제(2),끝내기(3) : 1 엔터 입력시
# 저장이름: 이진수
# 전화번호: 0107777777    ==> 리스트 phone_list=['이진수','01077771111']
#전체보기(0),저장(1),삭제(2),끝내기(3) : 1 엔터 입력시
# 저장이름: 홍길동
# 전화번호: 01022225555
#전체보기(0),저장(1),삭제(2),끝내기(3) : 2 엔터 입력시
# 삭제할 이름 : 이진수 ==> phone_list.pop(인덱싱) 이진수 리스트가 삭제
#전체보기(0),저장(1),삭제(2),끝내기(3) : 0 엔터 입력시
#['홍길동','01022225555']

# count : phone_list의 인덱싱으로 사용할 변수, 삭제시 phone_list.pop
# input으로 입력받은 삭제할 이름(del_ch)이 리스트(count)의 존재한다면 삭제하고,
# 그렇지 않으면 count를 증가해서 다음 요소를 검사한다.

# 전체보기 출력 값은 한줄단위로 출력하고요. 반드시 sorted 로 오름차순으로 보이도록 출력

# phone_list.append([add_name, add_phone])
    
from calendar import c


print("전화번호 저장, 전체보기")
phone_list = []
while True:
    sel_ch = int(input("전체보기(0),저장(1),삭제(2),끝내기(3): "))
      
    if sel_ch == 0:     
        for i in phone_list:
            print(i)
    elif sel_ch == 1:
        add_name = input("저장이름: ")
        add_phone = str(input("전화번호: "))
        phone_list.append([add_name, add_phone])
        tmp = sorted(phone_list)
        phone_list = tmp
    elif sel_ch == 2:
        count = 0
        del_ch = input("삭제할 이름 : ")
        while True:
            if del_ch == phone_list[count][0]:
                phone_list.pop(count)
                break
            else:
                count += 1
                
    elif sel_ch == 3:
        print("종료합니다.")
        break