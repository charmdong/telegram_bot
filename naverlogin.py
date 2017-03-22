from selenium import webdriver
import time

login = webdriver.Firefox()
login.get("http://naver.com")
div = login.find_element_by_id("loginframe")
links=div.find_elements_by_tag_name('a')
links[0].click()

time.sleep(3)

elem=login.find_element_by_id('id')
elem.send_keys("chungdk1993")

time.sleep(2)

elem = login.find_element_by_id('pw')
elem.send_keys("dusalwjdthch")
elem.submit()

time.sleep(2)
"""
login.get("http://mail.naver.com")
login.get('https://mail.naver.com/?n=1489996881437&v=f#%7B%22fClass%22%3A%22write%22%2C%22oParameter%22%3A%7B%22orderType%22%3A%22new%22%2C%22sMailList%22%3A%22%22%7D%7D')

elem = login.find_element_by_id('toDiv')
elem.send_keys('chungdk1117@gmail.com')

elem = login.find_element_by_id('sguide')
elem.send_keys('TEST MAIL')

elem = login.find_element_by_id('se2_inputarea')
elem.send_keys('TEST')
elem.submit()
"""
