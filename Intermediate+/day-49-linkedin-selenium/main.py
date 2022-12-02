import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

chrome_driver_path = r"C:\Users\HP\development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
linked_in = "https://www.linkedin.com/jobs/search/?currentJobId=3142525612&f_AL=true&geoId=103801469&keywords=python%20developer&location=Varna%2C%20Bulgaria&refresh=true"
website = driver.get(url=linked_in)
sign_in = driver.find_element(By.XPATH, '/html/body/div[3]/header/nav/div/a[2]')
sign_in.click()
username = driver.find_element(By.XPATH, '//*[@id="username"]')
username.send_keys("simeon_sg@abv.bg")
password = driver.find_element(By.XPATH, '//*[@id="password"]')
password.send_keys("loopbymtel17")
sign_in_button = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
sign_in_button.click()
#easy_apply_btn = driver.find_element(By.CSS_SELECTOR, 'div div .jobs-apply-button--top-card')
#easy_apply_btn.click()
#phone_number = driver.find_element(By.XPATH, '//*[@id="urn:li:fs_easyApplyFormElement:(urn:li:fs_normalized_jobPosting:3142525612,6201399360701077642,phoneNumber~nationalNumber)"]')
#phone_number.send_keys("+359893444257")
#last_btn = driver.find_element(By.XPATH, '//*[@id="ember376"]/span')
#last_btn.click()
top_container = driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")
for element in top_container:
    element.click()
    time.sleep(5)
    try:
        easy_apply_btn = driver.find_element(By.CSS_SELECTOR, '.jobs-s-apply button')
        easy_apply_btn.click()
        time.sleep(5)
        phone_number = driver.find_element(By.XPATH, 'fb-single-line-text__input')
        if phone_number == "":
            phone_number.send_keys("+359893444257")
            submit_button = driver.find_element(By.CSS_SELECTOR, "footer button")
            if submit_button.get_attribute("data-control-name") == "continue_unify":
                close_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
                close_button.click()
                time.sleep(2)
                discard_button = driver.find_elements(By.CLASS_NAME,"artdeco-modal__confirm-dialog-btn")[1]
                discard_button.click()
                print("Complex application, skipped.")
                continue
            else:
                submit_button.click()

                # Once application completed, close the pop-up window.
            time.sleep(2)
            close_button = driver.find_element(By.CLASS_NAME,"artdeco-modal__dismiss")
            close_button.click()

            # If already applied to job or job is no longer accepting applications, then skip.
    except NoSuchElementException:
        print("No application button, skipped.")
        continue
time.sleep(5)
driver.quit()


