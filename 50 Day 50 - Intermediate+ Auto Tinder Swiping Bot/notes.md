### 424 Day 50 Goals_ what you will make by the end of the day

Steps (Including the ones for those that does not have a tinder acc)
1. Get a fake photo
2. Create a profile on Tinder
3. Click I Accept
4. Log In 
5. Swipe Right on everybody
6. When there is a match, click back to tinder
7. Repeat from 3


Tinder taking time to send verification code on phone, so using this fake tinder instead - 
[https://pablorotten.github.io/fake-tinder/](https://pablorotten.github.io/fake-tinder/)

Using the fake tinder app, this is the code - 

```python
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
```

***1. Get a fake photo***

Using my own photo

***2. Create a profile on Tinder***

Created

***2a. Go to the website***

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
driver.get("https://tinder.com/")
```

***3. Click "I Accept""***
```python
accept = driver.find_element(By.XPATH, '//*[@id="s1477815459"]/div/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]')
accept.click()
```

***4. Click Log In***

```python
login = driver.find_element(By.XPATH, '//*[@id="s1477815459"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]')
login.click()
```

***4a. Click 'Login with Google'***

**The Login button for google is basically an iframe, so it is a few extra steps.**
**Let's do login with FB**

***4b. Click 'Login with FB'***

```python
fb_btn = driver.find_element(By.XPATH, '//*[@id="q1211014382"]/main/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button/div[2]/div[2]/div/div')
fb_btn.click()
```

Another window opens. This is called a child window.
Selenium now must focus on this child window to access the elements there.

From the doc - 
>*Clicking a link which opens in a new window will focus the new window or tab on screen, 
> but WebDriver will not know which window the Operating System considers active. 
> To work with the new window you will need to switch to it. 
> If you have only two tabs or windows open, and you know which window you start with, by the process of elimination 
> you can loop over both windows or tabs that WebDriver can see, and switch to the one which is not the original.*

*We can do this by*
```python
driver.window_handle
#this gets the current window in focus
driver.window_handles
#this gets a list of the windows open, starting from the main one.
driver.switch_to.window(window_name=)
#this switches to the windpw specified
```

So the code is -
```python
driver.switch_to.window(driver.window_handles[1])
```

From there on it is pretty simple, you find the elements and send the keys, i.e. input the credentials.

```python
email_input = driver.find_element(By.XPATH, '//*[@id="email"]')
email_input.send_keys('rough.rafi@gmail.com')
pass_input = driver.find_element(By.XPATH, '//*[@id="pass"]')
pass_input.send_keys('112358132134')
pass_input.send_keys(Keys.ENTER)
```

***Login Done***