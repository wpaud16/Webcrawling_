from selenium import webdriver
# 웹 창에 입력을 하기 위함
from selenium.webdriver.common.keys import Keys

# () 안에 주소 경로 적어줘야 하는데 지금은 같은 폴더에 있으니까 안해줘도 됨
browser = webdriver.Chrome()
# 전체 화면으로 띄어줌
browser.maximize_window()
# 크롬 브라우져에서 get 주소에 있는 곳으로 이동함
browser.get("http://naver.com")

# elem 에 브라우져에 있는 네이버에서 태그 중 클래스 이름이 "link_login" 인 정보를 저장하고
elem = browser.find_element_by_class_name("link_login")
# 위 정보를 클릭한다
elem.click()

# 이전 페이지로 이동
browser.back()
# # 다시 앞으로 이동
browser.forward()
# # 새로 고침
browser.refresh()
# 브라우저 탭만 닫기
browser.close()
# 브라우져 전체를 닫기
browser.quit()

######################################################################

# elem 에서 id가 "query" 인 정보를 선택
elem = browser.find_element_by_id("query")

# 입력할 내용 적는 곳
elem.send_keys("이제명")

# enter 치는 코드
elem.send_keys(Keys.ENTER)

# a 태그 모두 가져옴
elem = browser.find_elements_by_tag_name("a")

########################################################################

# 다시 네이버 창으로 돌아옴
browser.back()

# 켜진 브라우져에서 클래스 이름 찾고 클릭까지 함
browser.find_element_by_class_name("link_login").click()

# 로그인 브라우져에서 또 아이디 찾아서 선택하고 클릭하고 정보까지 입력
browser.find_element_by_id("id").send_keys("네이버 아이디")
browser.find_element_by_id("pw").send_keys("네이버 비밀번호")

# 로그인 버튼 누르기
browser.find_element_by_id("log.login").click()

# id 창에 있는 내용을 지운다
browser.find_element_by_id("id").clear()