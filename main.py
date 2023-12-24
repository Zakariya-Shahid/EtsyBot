from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from time import sleep

urls = open("urls.txt", "r").read().split("\n")
username = "zakariyashahid511@gmail.com"
password = "BW-:dy-3=466V7t"
current_page = 1

def signin(driver):
    driver.get("https://etsy.com")
    # Find the button using its class name
    button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[class="wt-btn wt-btn--small wt-btn--transparent wt-mr-xs-1 inline-overlay-trigger signin-header-action select-signin header-button"]')))
    # Perform actions on the button (e.g., click)
    button.click()
    sleep(2)
    # Find the username box using its name attribute
    username_box = driver.find_element(By.ID, 'join_neu_email_field')
    # Send username information (keys) to element
    username_box.send_keys(username)
    # Find the password box using its name attribute
    password_box = driver.find_element(By.ID, 'join_neu_password_field')
    # Send password information (keys) to element
    password_box.send_keys(password)
    # Find the login button using its class name
    login_button = driver.find_element(By.CSS_SELECTOR, 'button[class="wt-btn wt-btn--primary wt-width-full"]')
    # Perform actions on the button (e.g., click)
    login_button.click()
    sleep(10)

def next_page(driver):
    global current_page
    try:
        next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'pager-next')))
        next_button.click()
        current_page += 1
    except:
        pass


def follow(driver):

    follow_buttons = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'follow-btn-container')))
    for follow_button in follow_buttons:
        follow_button.click()
        sleep(2)


def operator(driver):
    global current_page
    while current_page < 15:
        follow(driver)
        previous_page = current_page
        next_page(driver)
        if previous_page == current_page:
            break

    current_page = 1

if __name__ == "__main__":
    driver = webdriver.Chrome()
    signin(driver)
    while True:
        for url in urls:
            driver.get(url)
            operator(driver)
        # sleep of 24 hours
        sleep(86400)

    driver.close()
