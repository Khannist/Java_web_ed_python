from urllib import response
from bs4 import BeautifulSoup
from urllib.request import urlopen

response = urlopen('https://www.naver.com/') #response는 단순 변수
soup = BeautifulSoup(response, 'html.parser') #html.parser 추출기
for anchor in soup.find_all('a'):
    print(anchor.get('href','/'))
    
# Beautifulsoup를 이용한 영화박스오프시 가져오기
# response = urlopen('https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%98%81%ED%99%94%EB%B0%95%EC%8A%A4%EC%98%A4%ED%94%BC%EC%8A%A4&oquery=%EC%98%81%ED%99%94+%EB%B0%95%EC%8A%A4+%EC%98%A4%ED%94%BC%EC%8A%A4&tqi=hCY22lprvN8ssRsE5alssssstgZ-478604')

# soup = BeautifulSoup(response,'html.parser')
# i = 1
# f = open("movie_rank.txt", 'w', encoding='utf-8')
# for anchor in soup.select('div.title_box'):
#     data = str(i) + "위 : " + anchor.get_text() + "\n"
#     i = i + 1
#     f.write(data)
# f.close

# i = 1
# for anchor in soup.select("div.title_box"):
#     data = str(i) + "위 : " + anchor.get_text()
#     i = i + 1
#     print(data)