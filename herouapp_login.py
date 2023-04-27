#import selenium
from selenium import webdriver
import os

url = 'https://the-internet.herokuapp.com/login'
os.environ['PATH'] += r'C:/chromedriver'
driver =webdriver.Chrome()
driver.get(url)

Username = driver.find_element_by_id('username')
Username.send_keys('tomsmith')

Password = driver.find_element_by_id('password')
Password.send_keys('SuperSecretPassword!')

login = driver.find_element_by_css_selector('button[type="submit"]')
login.click()