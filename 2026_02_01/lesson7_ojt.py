from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

option = webdriver.ChromeOptions()
# 避免瀏覽器自動關閉
option.add_experimental_option( 'detach', True )
prefs = { 'profile.default_content_setting_values': { 'notifications': 2 } }
option.add_experimental_option( 'prefs', prefs )
driver = webdriver.Chrome( service = Service( executable_path = ChromeDriverManager().install() ), options = option )
driver.get( 'https://ojt.wda.gov.tw/ClassSearch' )

# 課程查詢
driver.find_element( By.CSS_SELECTOR, 'input[id="Form_PlanType_1"]' ).click()
# 等待( 瀏覽器, 秒數 ) .直到( 判斷 元素可定位 定位目標元素 )
keyWait = WebDriverWait( driver, 10 ).until( EC.presence_of_element_located( ( By.CSS_SELECTOR, 'input[id="Form_KEYWORDS"]') ) )
keyWait.send_keys('大數據')
# 下拉式選單
Select( driver.find_element( By.CSS_SELECTOR, 'select[name="Form.STDATE_YEAR_SHOW"]' ) ).select_by_index( 1 )
Select( driver.find_element( By.CSS_SELECTOR, 'select[name="Form.STDATE_MON"]' ) ).select_by_value( '1' )
Select( driver.find_element( By.CSS_SELECTOR, 'select[name="Form.FTDATE_YEAR_SHOW"]' ) ).select_by_index( 3 )
Select( driver.find_element( By.CSS_SELECTOR, 'select[name="Form.FTDATE_MON"]' ) ).select_by_value( '12' )

# CSS_SELECTOR  # main_form > div > div.unit-border > div.submit-bar > button.btn-orange
# XPATH         # //*[@id="main_form"]/div/div[2]/div[4]/button[1]
# FULL XPATH    # /html/body/div[4]/form[1]/div/div[2]/div[4]/button[1]
# XPath 範例
# driver.find_element( By.XPATH, '//*[text()="送出"]' ).click()
# 觀察選項
#se = Select( driver.find_element( By.CSS_SELECTOR, 'input[name="Form.STDATE_YEAR_SHOW"]' ) )
#for s in se.options:
#    print( s.text )
driver.find_element( By.CSS_SELECTOR, 'button[class="btn-orange"]' ).click()
#driver.find_element( By.CSS_SELECTOR, 'button[class="btn btn-info btn-info-Confirm"]' ).click()
# 關閉彈跳視窗(Esc)
webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()

# 取得網頁原始碼
soup = BeautifulSoup( driver.page_source, 'html.parser' )
print( soup )