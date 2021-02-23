# 웹 스크레핑 (내가 필요한 부분만 끌어오는 것) vs 웹 크롤링 (다 쓸어 담는 것)
# xpath  내가 클릭해야 할 부분을 클릭하고 검사 눌러서 html 코드에서 오른쪽 키 누르고 copy xpath 또는 fullpath 누르면 주소가 복사됨
import requests
import re  # 정규식 라이브러리 가져옴 쓰는 이유는 class 명을 쓸 때 가져옴

url = "http://nadocoding.tistory.com"
# user agent 는 기계가 접속 못하게 막혀있는 html 을 가져올 수 있도록 해주는 것!
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"}

# get 안에 있는 주소의 html을 가져오는 것
res = requests.get(url, headers=headers)
# 문제가 생겼을 땐 오류를 알려주고 실행을 멈춤 이걸 쓰는 걸 추천
res.raise_for_status()

# .status_code했을 때 200(.status_code.ok) 이면 잘 가져왔다는 뜻 // 403이면 권한이 없다
# print("응답코드" ,res.status_code)

# 가져온 html 의 글자수
print(len(res.text))

# 가져온 html 을 html 파일로 만들어서 보는 코드
with open("../_Webcrawling_project/nadocoding_html.html", "w", encoding="utf8") as t:
    t.write(res.text)

# "." (ca.e) 은 하나의 문자를 의미함 ex) cave, case... | caffe (x)
# "^" (^de) 은 문자열의 시작을 의미함 ex) desk, destnation... | fade (x)
# "$" (se$) 은 문자열의 끝을 의미함 ex) case, base ... | face (x)
p = re.compile("ca.e")


# 매치하는 안 하는지 함수화
def match_print(m):
    if m:
        print("m.group: ", m.group())  # 맞는 애만 출력
        print("m.string: ", m.string)  # 입력받은 문자열을그대로 출력
        print("m.start(): ", m.start())  # 일치하는 문자열의 시작 인덱스 // 공백 포함
        print("m.end: ", m.end())  # 일치하는 문자열의 끝 인덱스 // 공백 포함
        print("m.span(): ", m.span())  # 일치하는 문자열의 시작 / 끝 인덱스  //공백 포함
    else:
        print("매치되지 않음")


# 1. 가져온 거랑 매치하는지 보는 것 //  주어진 문자열의 처음부터 일치하는지 확인 caseless 도 된다고 함
m = p.match("case")
match_print(m)

# 2. 주어진 문자열 중에 일치하는 게 있는지 확인 // good care, careless 도 됨
m = p.search("good care")
match_print(m)

# 3. 일치하는 모든 것을 "리스트" 형태로 반환
lst = p.findall("careless cafe")
print(lst)
