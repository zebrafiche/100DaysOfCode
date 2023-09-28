from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3718418776&f_AL=true&f_E=1&f_WT=2&geoId=92000000&"
           "keywords=python%20developer&location=Worldwide&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&sortBy=R")

time.sleep(5.0)
sign_in_button = driver.find_element(By.CLASS_NAME, 'cta-modal__primary-btn')
sign_in_button.click()

email_field = driver.find_element(By.ID, 'username')
email_field.send_keys('rafi.abdullah.112358@gmail.com')

pass_field = driver.find_element(By.ID, 'password')
pass_field.send_keys('Fotkabazz1123581321')
pass_field.send_keys(Keys.ENTER)

time.sleep(5.0)

job_cards = driver.find_elements(By.CLASS_NAME, 'jobs-search-results__list-item')
for jobs in job_cards:
    jobs.click()
    time.sleep(3.0)
    try:
        easy_apply = driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div[4]/div/div/main/div/div[2]/div/div[2]/'
                                                   'div[1]/div/div[1]/div/div[1]/div[1]/div[4]/div/div/div/button/span')
        easy_apply.click()
    except NoSuchElementException:
        print('Easy Apply not found')
        continue
    time.sleep(5.0)

    try:
        submit_button = driver.find_element(By.XPATH, '//*[@id="ember495"]/span')
        submit_button.click()
    except NoSuchElementException:
        print("Submit button not found")
        cancel_icon = driver.find_element(By.CSS_SELECTOR, '#artdeco-modal-outlet button li-icon svg')
        cancel_icon.click()
        discard_button = driver.find_element(By.CSS_SELECTOR, '.artdeco-modal__actionbar button span')
        discard_button.click()




    
