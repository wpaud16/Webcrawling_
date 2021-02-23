import re
import csv
import requests
from bs4 import BeautifulSoup

# 네이버 코스피 시가총액 순위 200위

filename = "시가총액 1-200등까지.csv"
# newline 을 공백으로 하는건 원래는 한줄 들어가고 자동으로 한줄을 건너 뛰는데 공백으로 하면 안건너뜀
f = open(filename, "w",encoding='utf-8-sig', newline="")
writer = csv.writer(f)

# \t 문자를 기준으로 나눠서 리스트에 저장됨
title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE".split("\t")
writer.writerow(title)

for year in range(1,5):
    url = f"https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page={year}"

    res = requests.get(url)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "lxml")

    data_rows = soup.find("table", attrs={'class' : 'type_2'}).find("tbody").find_all("tr")

    for row in data_rows:
        cloums = row.find_all("td")
        # 의미 없는 줄 나눔 애들 제거
        if len(cloums) <= 1:
            continue
        # 각 행에 있는 데이터 정보를 줄바꿈 문자를 제거한 형태로 리스트에 담아서 출력
        data = [cloum.get_text().strip() for cloum in cloums]

        # 리스트 형태의 변수를 집어 넣줘야 한다
        writer.writerow(data)
