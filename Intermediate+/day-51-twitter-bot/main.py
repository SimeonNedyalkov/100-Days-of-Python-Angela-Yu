from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

PROMISED_DOWN = 150
PROMISED_UP = 10
CHROME_PATH = r"C:\Users\HP\development\chromedriver.exe"
SPEED_PATH = "https://www.speedtest.net/"


class InternetSpeedTwitterBot:
    def __init__(self,driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get(SPEED_PATH)
        self.driver.maximize_window()
        self.driver.find_element(By.CSS_SELECTOR, "div #onetrust-accept-btn-handler").click()
        self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a').click()
        time.sleep(60)
        self.down = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.up = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text



    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/")
        self.driver.maximize_window()
        time.sleep(10)
        self.driver.find_element(By.CLASS_NAME, 'r-1ny4l3l').click()


bot = InternetSpeedTwitterBot(CHROME_PATH)
bot.get_internet_speed()
bot.tweet_at_provider()


"""
time.sleep(5)
google_login = driver.find_element(By.CSS_SELECTOR, 'div .hJDwNd-SxQuSe')
google_login.click()
"""
