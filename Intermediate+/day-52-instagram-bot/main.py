from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException

CHROME_PATH = r"C:\Users\HP\development\chromedriver.exe"
instagram_url= "https://www.instagram.com/accounts/login/"
RECOVERY_CODE = "39854217"

class Instafollower:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_PATH)

    def login(self):
        self.driver.get(url=instagram_url)
        self.driver.find_element(By.XPATH, '/html/body/div[4]/div/div/button[1]').click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys("simeonpythontest@gmail.com")
        self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys("Loopbymtel17@")
        self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button/div').click()
        time.sleep(10)
        #self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/div/div[1]/div[2]/form/div[4]/button').click()
        #self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/div/div[1]/div[2]/form/div[1]/div/label/input').send_keys(RECOVERY_CODE)
        #self.driver.find_element(By.XPATH,'//*[@id="react-root"]/section/main/div/div/div[1]/div[2]/form/div[2]/button').click()
        #time.sleep(10)
        self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/div/button').click()
        time.sleep(10)
        self.driver.find_element(By.CSS_SELECTOR, '._a9_1').click()

    def find_followers(self):
        time.sleep(5)
        self.driver.get(url="https://www.instagram.com/bboythesis/")
        time.sleep(6)
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/header/section/ul/li[2]/a/div').click()
        time.sleep(5)
        button = self.driver.find_element(By.CSS_SELECTOR, 'button._acan._acap._acas')
        for i in range(10):
            button.send_keys(Keys.PAGE_DOWN)
            time.sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, 'button._acan._acap._acas')
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                self.driver.find_element(By.XPATH,'/html/body/div[5]/div/div/div/div[3]/button[2]').click()

instagram = Instafollower()
instagram.login()
instagram.find_followers()
instagram.follow()
