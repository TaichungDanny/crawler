from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium_stealth import stealth
import undetected_chromedriver as uc
import PIL
from PIL import ImageGrab
from PIL import Image
import ddddocr
import time
import winsound
import random
import json

url = input('請輸入網址:')
ticnum = input('票數:')
state = input('是否隨機重整? ')

options = uc.ChromeOptions()
options.add_argument('--blink-settings=imagesEnabled=false')
driver = uc.Chrome(options=options)
chains = ActionChains(driver)
stealth(driver,
        languages=["zh-TW", "zh"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )

driver.get(url)
driver.maximize_window()
time.sleep(0.5)
login = driver.find_element(By.XPATH, "/html/body/header/div/div/div/div[5]/nav/div/div/a[3]")
login.click()
time.sleep(0.5)
login1 = driver.find_element(By.XPATH, "/html/body/div/div/form/div[7]/div")
login1.click()
time.sleep(0.5)
login2 = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input")
login2.send_keys('d033016@gmail.com')
time.sleep(0.5)
login3 = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div[1]/div/div/button/span")
login3.click()
input('press enter to continue')
while True:
    try:
        try:
            for e in driver.find_elements(By.CSS_SELECTOR, "button[class='btn btn-pink btn-buy']"):
                e.click()
        except:
            pass
        try:
            for i in driver.find_elements(By.CSS_SELECTOR, "td[class='action']"):
                i.click()
        except:
            pass
        time.sleep(0.5)
        select = Select(driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_DataGrid_ctl02_AMOUNT_DDL"))
        select.select_by_visible_text(ticnum)
        ocr = ddddocr.DdddOcr()
        img = ImageGrab.grab(bbox=(860, 665, 1045, 765))
        img.save('D:/Program Files/Sublime/Code/crawler/captcha/image.bmp')
        with open("D:/Program Files/Sublime/Code/crawler/captcha/image.bmp", 'rb') as f:
            image = f.read()
        res = ocr.classification(image)
        elem = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_CHK")
        elem.send_keys(res)
        a = str(driver.current_url)
        ele = driver.find_element(By.CSS_SELECTOR, "a[onclick='ImageCode_Verify();']")
        ele.click()
        time.sleep(0.5)
        if str(driver.current_url) == a:
            driver.refresh()
        else:
            input('press enter to continue')
    except:
        if state == 'Y':
            time.sleep(random.uniform(0.2, 2.2))
            driver.refresh()
            print('refreshing')
        else:
            driver.refresh()
            print('refreshingGGG')

