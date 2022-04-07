jn_mn = """
*********************
* 1. 회원가입       *
* 2. 회원검색       *
* 3. 회원탈퇴       *
* 0. 종료           *
*********************
"""
jn_sc = """
*****<검색항목>******
* 1. ID             *
* 2. 이름           *
* 3. 이메일 주소    *
* 이외. 검색취소    *
*********************
"""

db = [["sssss","1111111","sss","111111123","3213213123","42421412"],["ddddd","2353242","ddd","123","123","dsq@aw"],["awwww","42dsadqw","www","123","123","ww@ww"]]

def join():
    while True:
        a = True
        b = 0
        while True:
            ID = input("ID: ")
            if len(ID) < 5:
                print("5글자 이상 입력해주세요.")
            else:
                break
        for TID in db:
            b += 1
            if ID in TID:
                print("이미 존재하는 아이디입니다. 사용할 수 없습니다.")
                break
            if b >= len(db):
                a = False
        if a == False:
            break
    tdb = ID
        
    while True:
        pwd = input("P/W: ")
        if len(pwd) < 6 or len(pwd) >= 12:
            print("6글자이상 12글자미만으로 입력해주세요.")
        else:
            break
    tdb = tdb + " " + pwd    
    name = input("이름: ")
    tdb = tdb + " " + name
    addr = input("주소: ")
    tdb = tdb + " " + addr
    phn = input("전화번호: ")
    tdb = tdb + " " + phn
    ssnm = input("주민번호: ")
    tdb = tdb + " " + ssnm
    mail = input("이메일: ")
    tdb = tdb + " " + mail
    db.append(tdb.split( ))
    print(db)
    
def search():
    print(jn_sc)
    scho = int(input())
    if scho != 1 and scho != 2 and scho != 3:
        print("검색을 취소합니다.")
    else:
        b = ""
        if scho == 1:
            b = "ID"
        elif scho == 2:
            b = "이름"
        elif scho == 3:
            b = "이메일 주소"
        print(f"찾을 {b}를 입력하세요. ",end="")
        search_2(stmp = input())           

def search_2(stmp):
    a = 0
    for TID in db:
            if stmp in TID:
                print(db[a])
                break
            a+=1
            if a >= len(db):
                print("찾으시는 회원이 없습니다.")

def dele():
    a = 0
    dID = input("삭제할 ID를 입력하세요. ")
    for TID in db:
        if dID in TID:
            del db[a]
            print("삭제되었습니다.")
            break
        a+=1
        if a >= len(db):
            print("입력하신 ID가 없습니다.")
    
    
def main():
    while True:
        print(jn_mn)
        cho = int(input())
        
        if cho == 1:
            join()
        elif cho == 2:
            search()
        elif cho == 3:
            dele()
        elif cho == 4:
            for TID in db:
                print(TID)
        elif cho == 0:
            print("종료합니다.")
            break
       
main()
