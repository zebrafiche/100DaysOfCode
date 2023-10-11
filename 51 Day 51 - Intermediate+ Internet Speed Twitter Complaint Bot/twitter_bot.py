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







# element = driver.switch_to.active_element
# element.send_keys(Keys.ENTER)



