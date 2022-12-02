import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
from selenium.webdriver.common.keys import Keys
import csv

site_url = 'https://www.allrecipes.com/'
chrome_driver_path = r'C:\Users\HP\development\chromedriver.exe.exe'
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(site_url)
driver.maximize_window()
driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]').click()

articles = driver.find_elements(By.XPATH, '//*[@id="mntl-article_1-0"]/div')
divs = driver.find_elements(By.XPATH, '//*[@id="three-post__inner_1-0"]')
time.sleep(2)
def scrape_elements():
    for element in divs:
        time.sleep(2)
        #element.send_keys(Keys.CONTROL + 't')
        element.click()
        product = driver.find_element(By.CLASS_NAME, 'article-heading').text
        ingredients = driver.find_element(By.CLASS_NAME, 'mntl-structured-ingredients').text
        howtomake = driver.find_element(By.CLASS_NAME, 'mntl-recipe-intro').text
        recipe_steps = driver.find_element(By.CLASS_NAME, 'recipe__steps').text
        print(f'{product} \n {ingredients} \n {howtomake} \n {recipe_steps}')
        time.sleep(5)
        printstatement = f'{product},{ingredients},{howtomake},{recipe_steps}'
        with open('sami.csv', 'w', newline='',encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["product", "ingredients", "how to make"])
            writer.writerow([f"{product}", f'\n{ingredients}', f'\n{howtomake}', f'\n{recipe_steps}'])

scrape_elements()
# gameon = False
#
# while gameon == False:
#     scrape_elements()


time.sleep(600)
driver.quit()
