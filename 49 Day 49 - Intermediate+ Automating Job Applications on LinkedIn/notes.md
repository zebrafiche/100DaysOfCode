### 419 Day 49 Goals_ what you will make by the end of the day

We are going to use Selenium to create an automated job application bot for LinkedIn.

So basically we are going to apply to jobs that have the "Easy Apply" feature.

We are going to apply for a job at LinkedIn that Angela created, so as not to mess with other jobs.


***Steps*** - 
1. Open Browser on LinkedIn
2. Login with your credentials
3. Click on jobs
4. Using sendkeys method, apply for 'Python Developer' and 'Worldwide' in search 
5. Filter 'Remote' and 'Easy Apply'
6. Now you have the required list. For every job heading/div click on that link
7. Now click 'Easy Apply'
8. In the subsequent window, fill out the fields that are empty
9. Last window, select the top most resumes
10. Click Apply


Good Luck


### 420 Step 1 - Setup Your LinkedIn Account

Already have a LinkedIn account, so, done.


### 421 Step 2 - Automatically Login

1. Open Browser on LinkedIn
```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
driver.get("https://bd.linkedin.com/")
```

2. Login with your credentials
```python
email_field = driver.find_element(By.ID, 'session_key')
email_field.send_keys('rafi.abdullah.112358@gmail.com')

pass_field = driver.find_element(By.ID, 'session_password')
pass_field.send_keys('Fotkabazz1123581321')
pass_field.send_keys(Keys.ENTER)
```

Issue, two-factor authentication is on. 

3. Click on jobs
4. Using sendkeys method, apply for 'Python Developer' and 'Worldwide' in search 
5. Filter 'Remote' and 'Easy Apply'

For this I can just select the kind of jobs I want, and then copy that link to be used with Selenium, no need to code.
Issue - New landing page, new sign in button, new username and password field IDs.
So tweaked teh code a little.
```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3693361499&f_AL=true&f_E=2&f_WT=2&geoId=92000000&"
           "keywords=python%20developer&location=Worldwide&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&sortBy=R")

time.sleep(5.0)
sign_in_button = driver.find_element(By.CLASS_NAME, 'cta-modal__primary-btn')
sign_in_button.click()

email_field = driver.find_element(By.ID, 'username')
email_field.send_keys('rafi.abdullah.112358@gmail.com')

pass_field = driver.find_element(By.ID, 'password')
pass_field.send_keys('Fotkabazz1123581321')
pass_field.send_keys(Keys.ENTER)
```
6. Now you have the required list. For every job heading/div click on that link
```python
job_cards = driver.find_elements(By.CLASS_NAME, 'jobs-search-results__list-item')
for jobs in job_cards:
    jobs.click()
    time.sleep(5.0)
    # time.sleep() to allow for the job details to load on the right
```

7. Now click 'Easy Apply'

```python
for jobs in job_cards:
    jobs.click()
    time.sleep(3.0)
    easy_apply = driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div[4]/div/div/main/div/div[2]/div/div[2]/'
                                               'div[1]/div/div[1]/div/div[1]/div[1]/div[4]/div/div/div/button/span')
    easy_apply.click()
# note - this xpath has been collected from Firefox, not chrome, the chrome one did not work
```

I am not comfortable applying to every result, let's do save

```python
for jobs in job_cards:
    jobs.click()
    time.sleep(3.0)
    save = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div[4]/div/button/span[1]')
    save.click()
```

8. In the subsequent window, fill out the fields that are empty
9. Last window, select the top most resumes
10. Click Apply

_On second thought, let's apply._


***Applying to those only that do not have any subsequent windows. Also all the fields seems to be prefilled.***

>When finding element by CLASSNAME, NAME, TAGNAME, XPATH do not work, CSS_SELECTORS DO THE TRICK.

***HINT - Selenium has a custom exception that gets raised when an element cannot be found it's called 
NoSuchElementException. You'll need to import it to use it***

```python
from selenium.common.exceptions import NoSuchElementException

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
```


#### PUTTING IT ALL TOGETHER

```python
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
```

#### fin