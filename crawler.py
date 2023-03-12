from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

chromedriver = 'chromedriver.exe'
options = webdriver.ChromeOptions()
options.add_argument('ignore-certificate-errors')
driver = webdriver.Chrome(options=options)
chains = ActionChains(driver)
driver.get('https://tixcraft.com/activity/detail/23_atc')
time.sleep(5)
ele = driver.find_element(By.XPATH, '//*[@id="tab-func"]/li[1]/a/div')
ele.click()
time.sleep(2)
buy = driver.find_element(By.XPATH, '//*[@id="gameList"]/table/tbody/tr/td[4]/button')
buy.click()
time.sleep(5)
