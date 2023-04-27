import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

s = Service('C:/chromedriver.exe')
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])          # keep automation
chrome_options.add_experimental_option('useAutomationExtension', False)              # bot hidden on web
chrome_options.add_experimental_option("detach", True)        
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("--incognito")                              # keep active browser
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(chrome_options=chrome_options, service= s)
driver.implicitly_wait(5)
driver.maximize_window()

url = 'https://the-internet.herokuapp.com/login'

driver.get(url)

Username = driver.find_element(By.ID, 'username')
Username.send_keys('tomsmith')

Password = driver.find_element(By.ID, 'password')
Password.send_keys('SuperSecretPassword!')

login = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
login.click()
