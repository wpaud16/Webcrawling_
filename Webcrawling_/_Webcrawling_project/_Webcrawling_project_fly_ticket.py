from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# 로딩 창 기다릴 때 필요한 것들
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://flight.naver.com/flights/?trip=RT&scity1=ICN&scity2=&ecity1=&ecity2=ICN&adult=1&child=0&infant=0&fareType=YC&airlineCode=&nxQuery=%ED%95%AD%EA%B3%B5%EA%B6%8C")

# 텍스트를 이용해서 선택
browser.find_element_by_link_text("가는날 선택").click()

# 이번달 27일 , 28일 선택 // 텍스트가 27인 모든 태그를 가져온다
browser.find_elements_by_link_text("27")[0].click() # 가는 날
browser.find_elements_by_link_text("28")[0].click() # 오는 날

# 상위 태그를 선택
browser.find_element_by_xpath('//*[@id="recommendationList"]/ul/li[1]').click()

# 항공권 검색
browser.find_element_by_link_text("항공권 검색").click()

# 로딩창이 있을 때 다음 동작을 수행하지 못하는 경우가 있는데 이때, 다음 엘리먼트가 나올 때 까지만 기다리라고 할 수 있다. // 최대 15초를 기다리는데 아래 XPATH 가 나올 때까지 기다린다 // 꼭 XPATH 아니여도 됨
try:
    elem = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, "//*[@id='content']/div[2]/div/div[4]/ul/li[1]"))) # 성공하면 아래 코드 실행
    print(elem.text) # 첫번째 결과에 대한 text들 출력
finally: # 위에 결과가 다 끝나면 종료
    browser.quit()


