### 411 Day 48 Goals_ what you will make by the end of the day

Today we will work with a new technology for advanced web scraping. Selenium Webdriver. 

Why chose Selenium Webdriver over Beautiful Soup?

Because with Selenium you can automate browsers, tell it to type, enter and click on certain buttons.
This is something that the Beautiful Soup cannot do.

### 412 How to Install & Set Up Selenium

Requirements
1. Chrome
2. Chrome Driver marching the version of chrome
3. Install and setup Selenium

_We will be using the chrome developer tool heavily today, so chrome._

_Download chromedriver, extract it, and store the path to the extracted file._

_Download selenium, create a driver instance using the chromedriver path as an argument._

Current chrome version is 117, chromedriver for which is not readily available.

***However, if you use latest selenium version v4.12.0, you do not have to worry about downloading the chromedriver 
manually, selenium's new in-built tool Selenium Manager will download and manage the drivers for you automatically.***

Code to launch browser can be as simple as:

```python
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.google.com/")
```

#### Selenium v4 compatible Code Block - 

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
```

Out of the box Selenium comes with the capability to work with various browsers.
How does it know which browser to work with, based on the code?
That is where the chromedriver comes in, it provides a bridge between selenium and chrome.

Now open a webpage

```python
driver.get("https://www.amazon.com")
```

> Browser opens but then closes immediately.

Because the code is done running, to keep the code running, we can use while loop, sleep etc.
We can also use - 

```python
driver.get("https://www.amazon.com")

input("Press ENTER to exit\n")
```

This way, until you press Enter, the code will be running.

driver.close() vs driver.quit()

Once you are done, you can close the program using any of the above.
driver.close() closes the single tab, driver.quit() closes the entire browser.


### 413 How to Find and Select Elements on a Website with Selenium

Now we will learn how to find and locate specific elements on the webpage.
Refer to the Amazon price tracker project, we will use the same thing using Selenium.

```python
driver.get("https://www.amazon.com/LEATHERMAN-Rebar-Multitool-Stainless-Sheath/dp/B005KSWIBQ/")
```

Selenium can find element by its properties, id, css, class etc.

```python
driver.get("https://www.amazon.com/Kirkland-Revitalizes-Follicles-Minoxidil-Siamproviding3/dp/B00T4WXPRU/")
price = driver.find_element(By.CLASS_NAME, 'a-price-whole')
print(price.text)
```
```
15
```

What else can we do to keep the browser running, apart from the input?
One way is to detach the browser from the python program's execution.

From StackOverflow
```python
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver=webdriver.Chrome(executable_path=chrome_driver_path,options=options)
```

Therefore in my code let's make the necessary changes

```python
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
```

Works, the browser does not close immediately.

Some links do not produce desired results because the price information is not accessible from BD.
Therefore, had to look for products that has price information, given the location is BD.
So settled for a matte screen protector for the kindle.

Also, for the find_element method to work, you will need to import 

_from selenium.webdriver.common.by import By_

```python
from selenium.webdriver.common.by import By
driver.get("https://www.amazon.com/dp/B09H4ZHXZ5")
price = driver.find_element(By.ID, 'price_inside_buybox')
print(price.text)
```

```
$10.99
```

You can also find elements by other properties

```python
product_name = driver.find_element(By.ID, 'productTitle')
print(product_name.id)
print(product_name.text)
print(product_name.tag_name)
```

```
5EC581C6837CFFBA9A155151EC485FFE_element_34
(3 Pack) Supershieldz Anti-Glare (Matte) Screen Protector Designed for All-new Kindle Paperwhite 6.8-Inch (11th Generation, 2021) / Kindle Paperwhite Signature Edition 6.8-Inch / Kindle Paperwhite Kids 6.8-Inch (11th Gen)
span
```

Now what if there is not any id or class for the tag/element?
We can also find elements by css selectors

```python
title = driver.find_element(By.CSS_SELECTOR, "#titleSection span")
print(title.text)
```

```
(3 Pack) Supershieldz Anti-Glare (Matte) Screen Protector Designed for All-new Kindle Paperwhite 6.8-Inch (11th
Generation, 2021) / Kindle Paperwhite Signature Edition 6.8-Inch / Kindle Paperwhite Kids 6.8-Inch (11th Gen)
```

Better yet, use find element by xpath
This is a very simple process, much simpler than any of the above
Find the element you want to scrape > inspect > locate the element > right click > copy > xpath

```python
price2 = driver.find_element(By.XPATH, '//*[@id="corePrice_desktop"]/div/table/tbody/tr/td[2]/span[1]/span[2]')
print(price2.text)
```
```
$10.99
```

***This is why chrome developer tools was suggested before, we can do a lot with it.***

### 414 Challenge_ Use Selenium to Scrape Website Data

Extract the upcoming event data from python.org website, and store them in a nested python dict.
The event data from python.org should be stored under the keys 'time' and 'name'

***Step 1 - Do the necessary imports***
```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
```
***Step 2 - Detach the browser from the code and launch the website***
```python
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
driver.get("https://www.python.org/events/python-events/")
```
***Step 3 - Create a list of event names***
```python
event_names = []
for event in driver.find_elements(By.CSS_SELECTOR, ".shrubbery h3 a"):
    event_names.append(event.text)
print(event_names)
```
```
['PyCon Uganda', 'Swiss Python Summit 2023', 'PyCon UK 2023', 'PyCon India 2023', 'PyConZA 2023', 'Django Day Copenhagen 2023']
```
***Step 4 - Create a list of event dates***
```python
dates = []
for date in driver.find_elements(By.CSS_SELECTOR, '.shrubbery li p time'):
    dates.append(date.text)
print(dates)
```
```
['21 Sept. – 23 Sept.', '21 Sept.', '22 Sept. – 25 Sept.', '29 Sept. – 02 Oct.', '05 Oct. – 06 Oct.', '06 Oct.']
```
>Note: When finding elements by CSS selector, I find that it is helpful to locate the element and then move up.
> 
> So if you are trying to locate ".shrubbery li p time", first type _time_(this is where your cursor is),
> then go up in the dev tools and find the immediately previous element, in this case _p_, and type p on the left of time,
> continue till you get to a class or id, which you can precede with . or #

***Step 5 - Create the dictionary with index numbers as keys, and sub-dicts containing date and name as values***
```python
event_dict = {}
for i in range(len(event_names)):
    event_details = {'date': dates[i], 'name': event_names[i]}
    event_dict[i] = event_details

print(event_dict)
```
```
{0: {'date': '21 Sept. – 23 Sept.', 'name': 'PyCon Uganda'}, 1: {'date': '21 Sept.', 'name': 'Swiss Python Summit 2023'}, 2: {'date': '22 Sept. – 25 Sept.', 'name': 'PyCon UK 2023'}, 3: {'date': '29 Sept. – 02 Oct.', 'name': 'PyCon India 2023'}, 4: {'date': '05 Oct. – 06 Oct.', 'name': 'PyConZA 2023'}, 5: {'date': '06 Oct.', 'name': 'Django Day Copenhagen 2023'}}
```

### 415 Challenge_ Use Selenium in a Blank Project & Scrape a Different Piece of Data

We are going to scrape wikipedia data.
Let's go to the wikipedia main page.

Challenge 1 - Scrape Number of Articles

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_count = driver.find_element(By.CSS_SELECTOR, '#articlecount a')
print(article_count.text)
```

```
6,717,190
```

### 416 How to Automate Filling Out Forms and Clicking Buttons with Selenium

So far we have only learned how to scrape data from websites using Selenium, i.e. .text method.
But Selenium can do much more.
Now we will see how to interact with links and other elements in a webpage.

***Click on the article_count element found before in the wikipedia page.***

```python
article_count.click()
```

Another method

```python
article_count = driver.find_element(By.LINK_TEXT, '6,717,190')
article_count.click()
```

***Search for something.***

We have to do an additional import for this
```python
from selenium.webdriver.common.keys import Keys
#this means that inside Selenium there is a folder called webdriver, inside which there is a folder called common
#which contains a folder called keys, which contains a class called Keys

search_bar = driver.find_element(By.NAME, 'search')
search_bar.send_keys('Python')
#The Keys class has a lot of constants, one of them is ENTER. There are other ones like SHIFT or TAB
search_bar.send_keys(Keys.ENTER)
```

***Signup to a website***

This is a dummy website created by Angela for the course.
The site has three text bars, first name, last name and email.
Then it has a button, called sign-up.

```python
driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.XPATH, '/html/body/form/input[1]')
first_name.send_keys('Abdullah')

last_name = driver.find_element(By.XPATH, '/html/body/form/input[2]')
last_name.send_keys('Al-Rafi')

email_add = driver.find_element(By.XPATH, '/html/body/form/input[3]')
email_add.send_keys('rough.rafi@gmail.com')

button = driver.find_element(By.CLASS_NAME, 'btn')
button.click()
```

### 417 The Cookie Clicker Project

### 418 Challenge_ Create an Automated Game Playing Bot

1. Go to the game website and familiarise yourself with how it works.
2. Create a bot using Selenium and Python to click on the cookie as fast as possible.
3. Every 5 seconds, check the right-hand pane to see which upgrades are affordable and purchase the most expensive one. 
You'll need to check how much money (cookies) you have against the price of each upgrade.
4. After 5 minutes have passed since starting the game, stop the bot and print the "cookies/second". e.g. this is mine.
5. Once you've managed to get the bot to work, feel free to tweak the algorithm if you think there is a better way to 
play the game. e.g. Change the time, instead of every 5 seconds to check the upgrades, what if you did every second. 
Or maybe the bot should buy all the affordable upgrades. Post your algorithm in the Q&A and impress us all if you 
manage to get a higher cookies/second with your algo.

```python
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
```

