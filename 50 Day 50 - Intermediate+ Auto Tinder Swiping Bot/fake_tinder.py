from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
driver.get("https://pablorotten.github.io/fake-tinder/")

like_button = driver.find_element(By.ID, "like")
dislike_button = driver.find_element(By.ID, "hate")

start = time.time()
end = start + 5

while time.time() <= end:
    like_button.click()
    dislike_button.click()


