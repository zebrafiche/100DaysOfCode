from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
driver.get("https://tinder.com/")

accept = driver.find_element(By.XPATH, '//*[@id="q-1355571838"]/div/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]')
accept.click()

login = driver.find_element(By.XPATH, '//*[@id="q-1355571838"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]')
login.click()

time.sleep(5.0)
print('ready')

fb_btn = driver.find_element(By.XPATH, '//*[@id="q1211014382"]/main/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button/div[2]/div[2]/div/div')
fb_btn.click()

driver.switch_to.window(driver.window_handles[1])

email_input = driver.find_element(By.XPATH, '//*[@id="email"]')
email_input.send_keys('rough.rafi@gmail.com')
pass_input = driver.find_element(By.XPATH, '//*[@id="pass"]')
pass_input.send_keys('112358132134')
pass_input.send_keys(Keys.ENTER)


