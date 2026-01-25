import json
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

option = webdriver.ChromeOptions()
# 避免瀏覽器自動關閉
option.add_experimental_option( 'detach', True )
prefs = { 'profile.default_content_setting_values': { 'notifications': 2 } }
option.add_experimental_option( 'prefs', prefs )
driver = webdriver.Chrome( service = Service( executable_path = ChromeDriverManager().install() ), options = option )
driver.get( 'https://www.facebook.com/' )

# 輸入帳號 / 密碼，登入
driver.find_element( By.CSS_SELECTOR, 'input[name="email"]' ).send_keys('')
driver.find_element( By.CSS_SELECTOR, 'input[name="pass"]' ).send_keys('')
driver.find_element( By.CSS_SELECTOR, 'button[name="login"]' ).click()

# 取得cookie
cookies = driver.get_cookies()
print( cookies, len(cookies) )
jsc = json.dumps( cookies )
# 將cookie寫入檔案
with open( 'fb_cookies.json', 'w' ) as f:
    f.write( jsc )
# 開啟FB新視窗，讀取cookie，登入facebook
driver = webdriver.Chrome( service = Service( executable_path = ChromeDriverManager().install() ), options = option )
driver.get( 'https://www.facebook.com/' )
with open( 'fb_cookies.json', 'r' ) as f:
    jscookies = f.read()
cookies = json.loads( jscookies )
for cookie in cookies:
    driver.add_cookie( cookie )
driver.refresh()


