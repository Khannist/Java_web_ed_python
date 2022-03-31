from calendar import c


def list_view():
    for i in phone_list:
        print(i)


def list_apd():
    add_name = input("저장이름: ")
    add_phone = str(input("전화번호: "))
    if len(add_name) != 0 and len(add_phone) != 0:
        phone_list.append([add_name, add_phone])
        tmp = phone_list
        phone_list = tmp
    else:
        print("입력을 정확하게 다시 해주세요!")


def list_pop():
    count = 0
    del_ch = input("삭제할 이름 : ")
    while True:
        if del_ch in phone_list[count]:
            phone_list.pop(count)
            break
        else:
            count += 1


print("전화번호 저장, 전체보기")
phone_list = []
while True:
    sel_ch = int(input("전체보기(0),저장(1),삭제(2),끝내기(3): "))

    if sel_ch == 0:
        list_view()
    elif sel_ch == 1:
        list_apd()
    elif sel_ch == 2:
        list_pop()
    elif sel_ch == 3:
        ans = input("정말로 끝내시겠습니까? (y/n) : ")
        if ans in ['y', 'Y']:
            print("종료합니다.")
            break
        else:
            continue
