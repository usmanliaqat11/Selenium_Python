import os
from selenium import webdriver
import pandas as pd

os.environ['PATH'] += r'C:/chromedriver'
driver = webdriver.Chrome()

url = 'https://www.youtube.com/c/JohnWatsonRooney/videos'
driver.get(url)

vidoes = driver.find_elements_by_class_name('style-scope ytd-grid-video-renderer')            ## scroll down must be used with mouse
you_list =[]                                                                                         #  Dynamic website!!
for data in vidoes:
    title = data.find_element_by_id('video-title').text
    views = data.find_element_by_xpath('.//*[@id="metadata-line"]/span[1]').text
    posted = data.find_element_by_xpath('.//*[@id="metadata-line"]/span[2]').text
    #print(title, views, posted)

    youtube_dict={
        "Title" : [title],
        "Views" : [views],
        "Posted" : [posted]
    }
    you_list.append(youtube_dict)

DataFrame = pd.DataFrame(you_list)
#print(DataFrame)
DataFrame.to_csv('youtube.csv')