from selenium import webdriver
import time

print("What will you search?")
search = input()

bro = webdriver.Firefox()
bro.get('http://google.com')

ele = bro.find_element_by_id('lst-ib')
ele.send_keys(search)
ele.submit()


