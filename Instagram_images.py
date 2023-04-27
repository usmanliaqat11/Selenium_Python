import os
import time
import wget                                                        # for downloading

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

os.environ['PATH'] += r'C:/chromedriverr'
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}              ## Handle alert chrome selenium driver !!!
chrome_options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(chrome_options=chrome_options)

url = 'https://www.instagram.com/'
driver.get(url)

username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="username"]')))
name = str(input('Email/PhoneNo :'))
username.send_keys(name)

password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[aria-label="Password"]')))
passwrd = str(input('Passwrd :'))
password.send_keys(passwrd)

login = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="loginForm"]/div/div[3]')))
login.click()

ads_notnow = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/div/button')))
ads_notnow.click()

search_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[aria-label="Search Input"]')))
search_btn.send_keys('#TheLionKing')

time.sleep(3)
search_h1 = driver.find_elements(By.CLASS_NAME, '_01UL2')
for h_1 in search_h1:
    lion_king = h_1.find_element(By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]')
    lion_king.click()

time.sleep(5)
body = driver.find_element(By.XPATH, '/html/body')
body.send_keys(Keys.PAGE_DOWN)
body.send_keys(Keys.PAGE_DOWN)

#                                     !!!    Starting   BS4   !!!

soup = BeautifulSoup(driver.execute_script('return document.documentElement.outerHTML'), 'html.parser')

list=[]
insta_page = soup.findAll('div', {'class': '_bz0w'})
#print(len(pagelinks))
for links in insta_page:
    all_links = links.find('img')['src']
    #print(all_links)
    list.append(all_links)
#                                    !!!   make directory  THE LION KING !!!

path = os.getcwd()
keyword = " TheLionKing "
path = os.path.join(path, keyword[1:])
os.mkdir(path)

for images in list:
    save_as = os.path.join(path, keyword[1:] + '.jpg')
    wget.download(images, save_as)                                      #       !!! download all the images in list  ###
