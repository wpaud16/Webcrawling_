import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

# 가져온 html 파일을 lxml 을 통해서 Beat- 라는 객체를 생성한 것
soup = BeautifulSoup(res.text, "lxml")

# 타이틀 태그를 다 가져옴
print(soup.title)

# 타이틀 태그에 있는 텍스트만 가져옴
print(soup.title.text)
print(soup.title.get_text())

# 처음 발견하는 a 태그를 출력함
print(soup.a)

# a 태그에 있는 href 값을 가져옴
print(soup.a["href"])

# 딕셔너리 형태로 가져옴
print(soup.a.attrs)

# a 태그 다 가져옴
print(soup.find_all("a"))

# a 태그에 해당하는 것을 가져오는데 클래스 속성이 "Nbtn_upload" 인 애 찾아달라
print(soup.find("a", attrs={"class": "Nbtn_upload"}))
print(soup.find(attrs={"class" : "Nbtn_upload"})) # a 태그 없애도 됨

# li 태그에 해당하는 것을 가져오는데 클래스 속성이 "rank01" 인 애 찾아서 rank01 에 저장하고 그 안에 있는 a 요소를 출력
rank1 = soup.find("li", attrs={"class": "rank01"})
print(rank1.a.text)

# 아래 형제 태그를 가져옴 한번만 하면 아마 개행 문자 때문에 아무것도 안 나옴
print(rank1.find_next_sibling("li"))  # == rank1.next_sibling.next_sibling

# 형제들을 '다' 가져옴
print(rank1.find_next_siblings("li"))

# 위에 형제 태그를 가져옴
print(rank1.find_previous_sibling("li"))  # == rank1.previous_sibling

# 부모 태그를 출력
print(rank1.parent)

# 글씨가 저거인 a 태그를 다 끌고 와라
webtoon = soup.find("a", text="연애혁명-337. 복병")
print(webtoon)


# 모든 웹툰 제목 끌고 옴
cartoons = soup.find_all("a", attrs={"class":"title"}) # 엄청 많음 놈임
for cartoon in cartoons:
    print(cartoon.get_text())

############################################################################################

url_1 = "https://comic.naver.com/webtoon/list.nhn?titleId=650305&weekday=sat"
res_1 = requests.get(url_1)
res_1.raise_for_status()

soup_1 = BeautifulSoup(res_1.text,"lxml")

#  호랑이 형님 페지에 있는 모든 제목 + 링크주소를 출력
cartoons_1 = soup_1.find_all("td", attrs={"class" : "title"})
for cartoon in cartoons_1:
    title = cartoon.a.get_text()
    link = cartoon.a['href']
    print(f"{title}: https://comic.naver.com{link}")

#평점 정보
cartoons_2 = soup_1.find_all("div", attrs={"class" : "rating_type"})
tot = 0
for cartoon in cartoons_2:
    rate = cartoon.find("strong").get_text()
    tot += float(rate)
mean = tot/len(cartoons_2)
print(f"호랭이 형님 근 10주 평점 평균 {round(mean,3)}") # 소수점 자리 수 제한

