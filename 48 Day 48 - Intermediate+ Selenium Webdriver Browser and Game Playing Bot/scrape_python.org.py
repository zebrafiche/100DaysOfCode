from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
driver.get("https://www.python.org/events/python-events/")

event_names = []
for event in driver.find_elements(By.CSS_SELECTOR, ".shrubbery h3 a"):
    event_names.append(event.text)
print(event_names)

dates = []
for date in driver.find_elements(By.CSS_SELECTOR, '.shrubbery li p time'):
    dates.append(date.text)
print(dates)

event_dict = {}
for i in range(len(event_names)):
    event_details = {'date': dates[i], 'name': event_names[i]}
    event_dict[i] = event_details

print(event_dict)
