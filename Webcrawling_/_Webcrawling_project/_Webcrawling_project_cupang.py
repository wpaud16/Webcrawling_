import requests
import re
from bs4 import BeautifulSoup

#첫번째 페이지
url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=1=4&backgroundColor="
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"}
res = requests.get(url   , headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

# search-product 로 시작하는 클래스 이름은 다 찾아오는 것 // 쿠팡 노트북 첫번째 페이지에 있는 노트북 정보 가져오는 것
items = soup.find_all("li", attrs={"class": re.compile('^search-product')})
for item in items:  # 찾아온 li 안에 태그들을 분리하는 것

    #로켓 배송을 빼고 출력
    rocket_items = item.find("span", attrs={"class": "badge rocket"})
    if rocket_items: #만약 로켓배송이면, 다시 위로 올라감
        continue

    name = item.find("div", attrs={"class": "name"}).get_text()  # 제품명
    price = item.find("strong", attrs={"class": "price-value"}).get_text()  # 가격
    rate = item.find("em", attrs={"class": "rating"})  # 평점

    if rate:  # none 이 아니면
        rate = rate.get_text()
    else:
        rate = "평점 없음"
    print(f"제품명: {name} \n가격: {price}\n평점: {rate}\n")

