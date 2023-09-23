from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_count = driver.find_element(By.CSS_SELECTOR, '#articlecount a')
print(article_count.text)

# article_count.click()

article_count = driver.find_element(By.LINK_TEXT, '6,717,200')
# article_count.click()

search_bar = driver.find_element(By.NAME, 'search')
search_bar.send_keys('Python')
search_bar.send_keys(Keys.ENTER)
