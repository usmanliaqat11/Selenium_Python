import os                                                                     ## VPN are neccessary to open website
import time                                                                             # VPN -> 'windscibe'

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote import switch_to
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

os.environ['PATH'] += r"C:/chromedriverr"
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}              ## Handle alert chrome selenium driver !!!
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.implicitly_wait(5)
driver.maximize_window()
url = 'https://pennie.com/'
driver.get(url)

saving_calculator = driver.find_element_by_css_selector('a[data-et-has-event-already="true"]')
saving_calculator.click()

time.sleep(5)
driver.switch_to.window(driver.window_handles[1])                              ## That are used to connect tabs & windows !!!
body = driver.find_element_by_xpath('/html/body')
body.send_keys(Keys.PAGE_DOWN)
body.send_keys(Keys.PAGE_DOWN)

time.sleep(2)
next = driver.find_element_by_css_selector('a[data-ng-click="agree()"]')
next.click()

zip_code = driver.find_element_by_css_selector('input[id="zipCode"]')
zip_code.send_keys('15234')

birth = driver.find_element_by_id('birthdate1')
birth.send_keys('10')
birth.send_keys('01')
birth.send_keys('1966')

income = driver.find_element_by_id('incomeValue')
income.send_keys('45000')

time.sleep(2)
btnn = driver.find_element_by_id('check-for-plans')
btnn.click()

next_1 = driver.find_element_by_id('providerSearchNext')
next_1.click()

time.sleep(2)
next_2 = driver.find_element_by_id('medicalUsageNext')
next_2.click()

next_3 = driver.find_element_by_id('prescriptionNext')
next_3.click()

view = driver.find_element_by_id('prescriptionSearchSubmit')
view.click()

check_boxes = driver.find_element_by_xpath('//*[@id="compareChk_6095"]')
check_boxes.click()

check_boxes_2 = driver.find_element_by_xpath('//*[@id="compareChk_6098"]')
check_boxes_2.click()

check_boxes_3 = driver.find_element_by_xpath('//*[@id="compareChk_5752"]')
check_boxes_3.click()

body = driver.find_element_by_xpath('/html/body')
body.send_keys(Keys.PAGE_DOWN)
body.send_keys(Keys.PAGE_DOWN)

compare_btn = driver.find_element_by_xpath('//*[@id="container"]/section/div[5]/aside/div[2]/div[3]/a')
compare_btn.click()

'//*[@id="compareChk_6095"]'
'//*[@id="compareChk_6098"]'
'//*[@id="compareChk_5752"]'


body.send_keys(Keys.PAGE_DOWN)
body.send_keys(Keys.PAGE_DOWN)
time.sleep(2)
benefits = driver.find_elements(By.CLASS_NAME, 'accordion-group')
body = driver.find_element_by_xpath('/html/body')
body.send_keys(Keys.PAGE_DOWN)
for i in range(4,len(benefits)+1):
    benefit = driver.find_element_by_xpath(f'//*[@id="benefitHead"]/div[4]/div[{i}]/div[1]/a')
    benefit.click()
    body.send_keys(Keys.ARROW_DOWN)
    body.send_keys(Keys.ARROW_DOWN)
    time.sleep(2)


soup = BeautifulSoup(driver.execute_script('return document.documentElement.outerHTML'), 'html.parser')                 ## That script are used to matchup (((  Selenium & BS4  )))
dict ={}
benefits = soup.findAll('div', {'class': 'accordion-inner'})
#print(benefits)
for benefit in benefits:
    header = benefit.findAll('div',{'class':'u-flex-25'})
    for i in header:
        if i != '\n':
            dict[i.text.strip()] = []
print(dict)
