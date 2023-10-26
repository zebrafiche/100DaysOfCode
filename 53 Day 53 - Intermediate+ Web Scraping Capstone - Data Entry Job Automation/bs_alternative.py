from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

zillow_url = input('Provide the link with all the filters applied - ')

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
driver.get(zillow_url)
driver.maximize_window()

# verification = driver.find_elements(By.XPATH, "//p[contains(text(), 'Press & Hold')]")
# ActionChains(driver).click_and_hold(verification).perform()

card = driver.find_elements(By.XPATH, "//article[@data-test='property-card']")
card.click()

