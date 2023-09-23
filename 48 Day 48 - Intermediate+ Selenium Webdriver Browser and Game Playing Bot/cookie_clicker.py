from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
driver.get("https://orteil.dashnet.org/cookieclicker/")
# take a small break before the screen loads
time.sleep(5.0)


language_eng = driver.find_element(By.XPATH, '//*[@id="langSelect-EN"]')
language_eng.click()
# take a small break before the screen loads
time.sleep(5.0)
cookie = driver.find_element(By.ID, 'bigCookie')


start = time.time()
# this is time now
session_end = start + 60
# this is end time

while time.time() <= session_end:
    click_start = time.time()
    # new start time
    click_session = click_start + 5
    # end time for clicking session
    while time.time() <= click_session:
        # while current time is less than the end time, keep clicking the cookie
        cookie.click()

    # Once the clicking has been done for 5 sec, you want to scroll to the bottom of the page for the unlocked items
    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Now find the most expensive item, in this case the one at the bottom of the list, and claim
    items_unlocked = driver.find_elements(By.CLASS_NAME, "unlocked")
    print(items_unlocked)
    # latest_item = items_unlocked[-1]
    # Alternatively, you can click on each available item
    for i in items_unlocked:
        i.click()

per_second = driver.find_element(By.ID, 'cookiesPerSecond')
print(per_second.text)


# One caveat, you have to scroll yourself to the bottom to make the unlocked items available
