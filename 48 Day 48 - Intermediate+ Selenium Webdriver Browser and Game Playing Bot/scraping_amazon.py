from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
driver.get("https://www.amazon.com/dp/B09H4ZHXZ5")
price = driver.find_element(By.ID, 'price_inside_buybox')
print(price.text)

product_name = driver.find_element(By.ID, 'productTitle')
print(product_name.id)
print(product_name.text)
print(product_name.tag_name)
title = driver.find_element(By.CSS_SELECTOR, "#titleSection span")
print(title.text)

price2 = driver.find_element(By.XPATH, '//*[@id="corePrice_desktop"]/div/table/tbody/tr/td[2]/span[1]/span[2]')
print(price2.text)
# input("Press ENTER to exit\n")

