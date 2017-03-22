from selenium import webdriver
import time

bro = webdriver.Firefox()
bro.get('http://google.com')

ele = bro.find_element_by_id('lst-ib')
ele.send_keys(input())
ele.submit()


