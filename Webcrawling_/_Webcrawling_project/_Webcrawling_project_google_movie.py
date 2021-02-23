from selenium import webdriver
import requests
import re
import time
from bs4 import BeautifulSoup

url = "https://play.google.com/store/movies/top"
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36",
           "Accept-Language" : "ko-KR,ko"}

interval = 2

browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)

res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

# 이렇게 받아오면 최초의 페이지에 있는 것들만 받아오는데 그래서 동적 페이지는 selenium 으로 해야 하는 것이다
movies = soup.find_all("div", attrs={"class" : "ImZGtf mpg5gc"})

for movie in movies:
    title = movie.find("div", attrs={"class" : "WsMG1c nnK0zc"})


# 스크롤 내리기 // 1080 은 pc 의 해상도(세로) 정보 == 1080 위치만큼 스크롤을 내려라
# browser.execute_script("window.scrollTo(0,1080)")

# 현재 문서 높이를 저장
pre_height = browser.execute_script("return document.body.scrollHeight")

while True:
    # 화면의 가장 아래로 스크롤 내리기
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    # 페이지 로딩
    time.sleep(interval)

    curr_height = browser.execute_script("return document.body.scrollHeight")

