import selenium
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

website = 'https://www.google.com/'
s = Service("D:/00INSTALL/chrome-win64/chromedriver-win64/chromedriver.exe")

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=s)
driver.get(website)

search = driver.find_element(by='xpath', value='//*[@id="APjFqb"]')
search.send_keys('House of Dragons')
search.send_keys(Keys.ENTER)
#search_button = driver.find_element(by='xpath', value='/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]').click()
#search_button
time.sleep(2)
driver.find_element(by='xpath', value='//*[@id="kp-wp-tab-overview"]/div[4]/div/div/div/div/div/div[1]/div/div/a/h3').click()
time.sleep(3)
driver.save_screenshot("D:/Python/WebScraping/screenshot.png")

