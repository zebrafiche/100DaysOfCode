from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.XPATH, '/html/body/form/input[1]')
first_name.send_keys('Abdullah')

last_name = driver.find_element(By.XPATH, '/html/body/form/input[2]')
last_name.send_keys('Al-Rafi')

email_add = driver.find_element(By.XPATH, '/html/body/form/input[3]')
email_add.send_keys('rough.rafi@gmail.com')

button = driver.find_element(By.CLASS_NAME, 'btn')
button.click()
