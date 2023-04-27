import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}              ## Handle alert chrome selenium driver !!!
chrome_options.add_experimental_option("prefs",prefs)

os.environ['PATH'] += r"C:/chromedriver"
driver = webdriver.Chrome(chrome_options=chrome_options)
url ="https://www.facebook.com/"
driver.get(url)

email = str(input("Email/phone_no :"))
emaill = driver.find_element_by_id('email')
emaill.send_keys(email)

password = str(input("Password :"))
passwd = driver.find_element_by_id('pass')
passwd.send_keys(password)

login = driver.find_element_by_css_selector('button[name="login"]')
login.click()

friend_requests = driver.find_element_by_css_selector('a[aria-label="Friends"]')
friend_requests.click()

def ftn():
    driver.get('https://www.facebook.com/friends')                                       ## get reqests
    page = driver.find_element_by_tag_name('html')
    page.send_keys(Keys.END)
    #time.sleep(2)
    main = driver.find_elements_by_css_selector('div[class="dati1w0a hv4rvrfc"]')
    #print(len(main))
    page = driver.find_element_by_tag_name('html')
    page.send_keys(Keys.END)
    for data in main:
        add_friend = data.find_elements_by_css_selector('div[class="rq0escxv l9j0dhe7 du4w35lb j83agx80 pfnyh3mw taijpn5t bp9cbjyn owycx6da btwxx1t3 kt9q3ron ak7q8e6j isp2s0ed ri5dt5u2 rt8b4zig n8ej3o3l agehan2d sk4xxmp2 d1544ag0 tw6a2znq oo1teu6h tv7at329"]')
        #print(len(datas))
        for i in add_friend:
            if i.text == 'Add Friend':
                driver.execute_script("arguments[0].click();", i)

        confirm = data.find_elements_by_css_selector('div[class="rq0escxv l9j0dhe7 du4w35lb j83agx80 pfnyh3mw taijpn5t bp9cbjyn owycx6da btwxx1t3 kt9q3ron ak7q8e6j isp2s0ed ri5dt5u2 rt8b4zig n8ej3o3l agehan2d sk4xxmp2 d1544ag0 tw6a2znq s1i5eluu tv7at329"]')
        # print(len(datas))
        for j in confirm:
            if j.text == 'Confirm':
                driver.execute_script("arguments[0].click();", j)

for i in range(15):
    ftn()
time.sleep(2)