import undetected_chromedriver as uc
import time
from selenium.webdriver.common.by import By
driver = uc.Chrome(headless=False,use_subprocess=False)
driver.get('https://addmefast.com/login')

# Checar URL
time.sleep(5)
if 'login' in driver.current_url:
    print('Login page')

# Capturar ID do Iframe do captcha
# div do id do iframe
id_iframe = driver.find_element(By.ID , 'turnstile-wrapper')
# printar html do div
html_div = id_iframe.get_attribute('innerHTML')
id_iframe = html_div.split('id="')[1].split('"')[0]
