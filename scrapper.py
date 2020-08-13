# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 19:04:14 2020

@author: USER
"""

from selenium import webdriver
import time
import sys

driver = webdriver.Chrome()
driver.get('https://www.instagram.com/p/CCv9YETJE_U/')
#driver.get(sys.argv[1])
time.sleep(3)

#if user not logined
try:
    close_button = driver.find_element_by_class_name('xqRnw')
    close_button.click()
except:
    pass


try:
    load_more_comment = driver.find_element_by_css_selector('.MGdpg > button:nth-child(1)')
    print("Found {}".format(str(load_more_comment)))
    i = 0
    while load_more_comment.is_displayed() and i < 10:
        load_more_comment.click()
        time.sleep(1.5)
        load_more_comment = driver.find_element_by_css_selector('.MGdpg > button:nth-child(1)')
        print("Found {}".format(str(load_more_comment)))
        i += 1
except Exception as e:
    print(e)
    pass

user_names = []
user_comments = []
comment = driver.find_elements_by_class_name('gElp9 ')
for c in comment:
    container = c.find_element_by_class_name('C4VMK')
    name = container.find_element_by_class_name('_6lAjh').text
    content = container.find_element_by_tag_name('span').text
    content = content.replace('\n', ' ').strip().rstrip()
    user_names.append(name)
    user_comments.append(content)

user_names.pop(0)
user_comments.pop(0)
import excel_exporter

with open('instacomments.csv','w',newline='',encoding="utf-8") as file:
        writer=csv.writer(file)
        writer.writerow(['user name','comments'])
for (x,y) in zip(user_names,user_comments):
    with open('instacomments.csv','a',newline='',encoding="utf-8") as file:
        writer=csv.writer(file)
        writer.writerow([x,y])

driver.close()