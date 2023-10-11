### 430 Day 51 Goals_ what you will make by the end of the day

So this is a bot that will test your internet speed and then tweet about it.

Steps
1. Go to speedtest.net
2. Handle the "Allow Location Access" popup
3. Click 'Go'
4. Wait for the speedtest to complete
5. Get the download and upload speeds and store them in a variable
6. Go to twitter
7. Log In
8. Post the download and upload speeds
9. Click "Post"


***1. Go to speedtest.net***

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
driver.get("https://www.speedtest.net/")
```

***2. Handle the "Allow Location Access" popup***

***3. Click 'Go'***

The window that opens, apparently does not ask for location access. Maybe because it opened in Chrome.
So let's handle the clicking Go part.

```python
go_btn = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
go_btn.click()
```

***4. Wait for the speedtest to complete***

We need to wait until the test results are available.

> From Stack Overflow
> 
> Link - https://stackoverflow.com/questions/59130200/selenium-wait-until-element-is-present-visible-and-interactable
> 
> If your use case is to validate the presence of any element, you need to induce WebDriverWait setting the 
> expected_conditions as presence_of_element_located() which is the expectation for checking that an element is 
> present on the Document Object Model (DOM) of a page. This does not necessarily mean that the element is visible. 
> So the effective line of code will be:
> 
>     WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".reply-button"))).click()```
> 
> If your use case is to extract any attribute of any element you need to induce WebDriverWait setting the 
> expected_conditions as visibility_of_element_located(locator) which is an expectation for checking that an element is 
> present on the DOM of a page and visible. Visibility means that the element is not only displayed, but it also has a 
> height and width that is greater than 0. So in your use case, effectively the line of code will be:
> 
>     email = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "element_css"))).get_attribute("value")
> 
> If your use case is to invoke click() on any element you need to induce WebDriverWait setting the expected_conditions 
> as element_to_be_clickable() which is an expectation for checking an element is visible and enabled such that you can 
> click it. So in your use case, effectively the line of code will be:
> 
>     WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".reply-button"))).click()


This works

```python
import time
time.sleep(60)
download_speed = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/'
                                               'div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
print(download_speed.text)
```

But I want to make this more efficient, wait until the element becomes visible and not more than that.

Also, the element is always visible actually, it just that during the test the value is set at '-'.
So the code prints '-'.

So we pick an element that becomes visible only after the test has been completed.

For example, an element by class name 'result-data' becomes visible only after the test.

```python
# Make the driver wait 300 seconds or until the result data is visible 
# (which is not visible until both dl and ul speeds have been calculated)
WebDriverWait(driver, 300).until(EC.visibility_of_element_located((By.CLASS_NAME, 'result-data')))
```

***5. Get the download and upload speeds and store them in a variable***

```python
download_speed = driver.find_element(By.CLASS_NAME, 'download-speed')
print(download_speed.text)

upload_speed = driver.find_element(By.CLASS_NAME, 'upload-speed')
print(upload_speed.text)
```

```
32.97
45.76
```

***6. Go to twitter***

```python
driver.get('https://twitter.com/')
```

***7. Log In***

```python
# Maximize window so the sign in button becomes visible
driver.maximize_window()

# click sign in
sign_in = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a/div')
sign_in.click()

# wait a few so that the sign in pop up/iframe becomes visible
WebDriverWait(driver, 300).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="modal-header"]/span/span')))

# enter username
username = driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
username.send_keys('zebrafiche')

# click next
next_btn = driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div/span/span')
next_btn.click()

# wait a few so that the password pop up/iframe becomes visible
WebDriverWait(driver, 300).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="modal-header"]/span/span')))

# enter pass
pass_input = driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
pass_input.send_keys('112358132134')

# click log in
login_btn = driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div')
login_btn.click()
```

***8. Post the download and upload speeds***

```python
# Wait until the homepage is visible
WebDriverWait(self.driver, 300).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[1]/div[1]/div[1]/div/div/div/div/div/div/h2/span')))
# Click on the post button
post = driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div')
post.click()
# Wait till the post box appears
WebDriverWait(driver, 300).until(EC.visibility_of_element_located((By.CLASS_NAME, 'public-DraftStyleDefault-block')))
# Find the post input and write something there
post_elem = driver.find_element(By.CLASS_NAME, 'public-DraftStyleDefault-block')
post_elem.send_keys('@zebrafiche')
# Wait till the name appears in the dropdown
time.sleep(3.0)
# Press enter to select the account you are tagging
post_elem.send_keys(Keys.ENTER)
# Type the remaining message
post_elem.send_keys(f'- upload speed is {a}, download speed is {b}')
```

***9. Click "Post"***

```python
post_btn = driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div[2]/div[4]/div/span/span')
post_btn.click()
```


### Putting it all together

main.py

```python
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
```

twitter_bot.py

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)


class twitter:
    def __init__(self):
        self.driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
        self.driver.get('https://twitter.com/')

    def maximize(self):
        # Maximize window so the sign in button becomes visible
        self.driver.maximize_window()

    def sign_in(self):
        # click sign in
        sign_in = self.driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a/div')
        sign_in.click()

        # wait a few so that the sign in pop up/iframe becomes visible
        WebDriverWait(self.driver, 300).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="modal-header"]/span/span')))

        # enter username
        username = self.driver.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        username.send_keys('zebrafiche')

        # click next
        next_btn = self.driver.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div/span/span')
        next_btn.click()

        # wait a few so that the password pop up/iframe becomes visible
        WebDriverWait(self.driver, 300).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="modal-header"]/span/span')))

        # enter pass
        pass_input = self.driver.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        pass_input.send_keys('112358132134')

        # click log in
        login_btn = self.driver.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div')
        login_btn.click()

        # Wait until the homepage is visible
        WebDriverWait(self.driver, 300).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[1]/div[1]/div[1]/div/div/div/div/div/div/h2/span')))

    def post(self, a, b):
        # Click on the post button
        post = self.driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div')
        post.click()

        # Wait till the post box appears
        WebDriverWait(self.driver, 300).until(EC.visibility_of_element_located((By.CLASS_NAME, 'public-DraftStyleDefault-block')))

        # Find the post input and write something there
        post_elem = self.driver.find_element(By.CLASS_NAME, 'public-DraftStyleDefault-block')
        post_elem.send_keys('@zebrafiche')
        time.sleep(3.0)
        post_elem.send_keys(Keys.ENTER)
        post_elem.send_keys(f'- upload speed is {a}, download speed is {b}')
        post_btn = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div[2]/div[4]/div/span/span')
        post_btn.click()
```

