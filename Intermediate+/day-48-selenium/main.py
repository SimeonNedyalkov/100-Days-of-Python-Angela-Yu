from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "C:\\Users\\HP\\developement\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(url="http://orteil.dashnet.org/experiments/cookie/")

game_on = False

cookie = driver.find_element(By.ID, 'cookie')

items = driver.find_elements(By.CSS_SELECTOR, "#store div")
items_id = [item.get_attribute("id") for item in items]
items_id.remove('buyElder Pledge')

time_seconds = time.time() + 5
timeout = time.time() + 60 * 5
element_index = 0

#Get all upgrade <b> tags

while game_on == False:
    cookie.click()
    items_b = driver.find_elements(By.CSS_SELECTOR, "#store b")
    buy_item = False
#Convert <b> text into an integer price.
    items = [item.text for item in items_b]
    items.remove('')
    item_prices = [int(price.split("-")[1].strip().replace(",", "")) for price in items]
#Get current cookie count
    money = int(driver.find_element(By.ID, 'money').text.replace(',', ''))
# Find upgrades that we can currently afford
    affordable_upgrages = []

    if time.time() > time_seconds:
        for price in item_prices:
            if money > price:
                element_index = item_prices.index(price)
                buy_item = True
                if buy_item:
                    new_item = driver.find_element(By.ID, items_id[element_index])
                    new_item.click()
                    buy_item = False
                    time_seconds = time.time() + 5
    if time.time() >= timeout:
        game_on = True
        cookies_per_second = driver.find_element(By.ID, "cps")
        print(cookies_per_second)

# Purchase the most expensive affordable upgrade
# After 5 minutes stop the bot and check the cookies per second count.
#driver.quit()
