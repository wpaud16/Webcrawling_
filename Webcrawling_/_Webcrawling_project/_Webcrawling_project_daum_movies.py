import requests
from bs4 import BeautifulSoup
import re

#2015-2019 년까지 상위 5개의 영화 이미지 저장
for year in range(2015,2020):

    url = f"https://search.daum.net/search?w=tot&q={year}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR"

    res = requests.get(url)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "lxml")

    post_images = soup.find_all("img", attrs={"class": "thumb_img"})

    # idx 에 0,1 이렇게 인덱스 값이 들어간다
    for idx, post_image in enumerate(post_images):
        # 주소를 가져온다
        img_url = post_image["src"]
        # 만약 "//" 로 시작한다면
        if img_url.startswith("//"):
            img_url = f"https:{img_url}"

        # 이미지에 대한 정보를 다시 불러옴
        img_res = requests.get(img_url)
        img_res.raise_for_status()

        # 사진을 저장하는 코드 // 이름이 같으면 덮어 쓰우는 걸 주의
        with open(f"movie{year}_{idx + 1}.jpg", "wb") as f:
            f.write(img_res.content)

        # 상위 5개만 가져온다
        if idx >= 4:
            break
