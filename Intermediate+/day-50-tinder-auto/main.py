from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
chrome_path = r"C:\Users\HP\development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_path)
driver.get(url="https://tinder.com/")
driver.maximize_window()
#WebDriverWait(driver,5).until(EC.element_to_be_clickable(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/button/span"))
vpishi_se = driver.find_element(By.XPATH, "data-testid='login'")
vpishi_se.click()
