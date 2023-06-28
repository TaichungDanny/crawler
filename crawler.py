from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from PIL import Image
import time
import random
import winsound

url = input('Entering url: ')
ticnum = input('Entering ticket number: ')
state = input('Automatically random refresh? (Y or N) ')


def check_exists_by_xpath(xpath):
    try:
        driver.find_element(By.XPATH, xpath)
        return True
    except NoSuchElementException:
        return False

chromedriver = 'chromedriver.exe'
options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
driver = webdriver.Chrome(options=options)
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
chains = ActionChains(driver)
driver.get(url)


while True:
    for i in driver.find_elements(By.CSS_SELECTOR, "font[color='#FF0000']"):
        try:
            i.click()
        except:
            continue
        if driver.current_url != url:
            chk = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[3]/div/div/div/form/div[3]')
            chk.click()
            select = Select(driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[3]/div/div/div/form/div[1]/table/tbody/tr/td[2]/select'))
            select.select_by_visible_text(ticnum)
            scroll_width = driver.execute_script('return document.body.parentNode.scrollWidth')
            scroll_height = driver.execute_script('return document.body.parentNode.scrollHeight')
            driver.set_window_size(scroll_width, scroll_height)
            driver.save_screenshot('image.png')
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



