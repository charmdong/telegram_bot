import time
from selenium import webdriver

#print('Input the keyword to search e-mail : ')
#search = input()

web = webdriver.Firefox()
web.get('http://naver.com')

div = web.find_element_by_id('loginframe')
link = div.find_elements_by_tag_name('a')
link[0].click()

time.sleep(3)

elem = web.find_element_by_id('id')
#my_id = input()
elem.send_keys("chungdk1993")

elem = web.find_element_by_id('pw')
#my_pass= input()
elem.send_keys("dusalwjdthch")
elem.submit()

time.sleep(2)

web.get('http://mail.naver.com')

div = web.find_element_by_id('nav_snb')
link = div.find_element_by_tag_name('a')
link.click()


time.sleep(2)
"""
elem = web.find_element_by_id('searchKeyWord')
elem.click()

elem.send_keys(search)

button = web.find_element_by_id('searchBtn')
button.click()
"""
elem = web.find_element_by_id('toDiv')
elem.send_keys(input())

elem = web.find_element_by_id('subject')
elem.send_keys(input())

button = web.find_element_by_id('sendBtn')
button.click()


