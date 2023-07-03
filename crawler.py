from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from PIL import ImageGrab
from PIL import Image
import time
import random
import winsound
import json
import cv2 as cv
import sys

url = input('Entering url: ')
ticnum = input('Entering ticket number: ')
state = input('Automatically random refresh? (Y or N) ')


def check_exists_by_xpath(xpath):
    try:
        driver.find_element(By.XPATH, xpath)
        return True
    except NoSuchElementException:
        return False


def captcha_recognize():
    img = "D:/Program Files//Sublime//Code//crawler//image.bmp"
    img_1 = cv.imread("image.bmp")
    if img_1 is None:
        sys.exit("Could not read the image.")
    else:
        cv.imshow("Display window", img_1)
        cv.waitKey(0)


chromedriver = 'chromedriver.exe'
options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
driver = webdriver.Chrome(options=options)
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
chains = ActionChains(driver)
with open('cookies.json') as f:
    cookies = json.load(f)
driver.get(url)
driver.maximize_window()


for cookie in cookies:
    driver.add_cookie(cookie)
driver.refresh()


while True:
    for i in driver.find_elements(By.CSS_SELECTOR, "font[color='#FF0000']"):
        try:
            i.click()
        except:
            continue
        if driver.current_url != url:
            time.sleep(4)
            chk = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[3]/div/div/div/form/div[3]/div')
            chk.click()
            select = Select(driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[3]/div/div/div/form/div[1]/table/tbody/tr/td[2]/select'))
            select.select_by_visible_text(ticnum)
            img = ImageGrab.grab(bbox=(730, 660, 840, 770))
            img.save('image.bmp')
            cap = captcha_recognize()
            # /html/body/div[2]/div[1]/div[3]/div/div/div/form/div[2]/div[2]/input

            order = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[3]/div/div/div/form/div[4]/button[2]')
            # order.click()
            # for i in range(10):
            #     winsound.PlaySound("beep.wav", winsound.SND_FILENAME)
            time.sleep(50)
        else:
            if state == 'Y':
                time.sleep(random.uniform(0.2, 1.2))
                driver.refresh()
                print('Refreshing!')
            else:
                driver.refresh()
                print('Refreshing!')

captcha_recognize()
time.sleep(50)



