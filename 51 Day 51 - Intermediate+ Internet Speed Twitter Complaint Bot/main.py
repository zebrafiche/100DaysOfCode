from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import twitter_bot

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
driver.get("https://www.speedtest.net/")

go_btn = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
go_btn.click()

# Make the driver wait 300 seconds or until the result data is visible
# (which is not visible until both dl and ul speeds have been calculated)
WebDriverWait(driver, 300).until(EC.visibility_of_element_located((By.CLASS_NAME, 'result-data')))

download_speed = driver.find_element(By.CLASS_NAME, 'download-speed')
print(download_speed.text)

upload_speed = driver.find_element(By.CLASS_NAME, 'upload-speed')
print(upload_speed.text)

bot = twitter_bot.twitter()
bot.maximize()
bot.sign_in()
bot.post(upload_speed.text, download_speed.text)
