from warnings import catch_warnings
import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common import by
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from urllib.parse import quote_plus    # 한글 텍스트를 퍼센트 인코딩으로 변환
from selenium import webdriver    # 라이브러리에서 사용하는 모듈만 호출
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException    # 태그가 없는 예외 처리
import pandas as pd
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
import googletrans
translator = googletrans.Translator()
item = ["ko=>en", "en=>ko"] #0/14
titletext = ''
def trans(text):#번역기
    try:
        if not text.encode().isalpha():#한글=>영어
            return str.lower(translator.translate(text, dest='en').text).split(" ")
        else:#영어=>한글
            return str.lower(translator.translate(text, dest='ko').text).split(" ")
    except:
        print("번역 에러")
while True:
    f = input("구글:")
    time0 = time.time()  
    print(trans(f)[0])
    print(time.time() - time0) 

url = 'http://b.classcard.net/Home/battle_enter'
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome('chromedriver', options=options)
driver.get(url)
code = str(input())
driver.find_element_by_id("battel_id").send_keys(code)
driver.find_element_by_id("battel_id").send_keys(Keys.ENTER)
time.sleep(0.5)
name = "10527이예준"
driver.find_element_by_id("user_name").send_keys(name)
driver.find_element_by_id("user_name").send_keys(Keys.ENTER)
while True:
    input()
    element = driver.find_elements_by_xpath("//input[@class='title']")
    print(element)
drver.quit() 