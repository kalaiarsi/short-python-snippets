from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from random import sample

browser=webdriver.Firefox()
browser.get("https://gabrielecirulli.github.io/2048/")
elem=browser.find_element_by_tag_name("html")
keys_options=[Keys.LEFT,Keys.UP,Keys.RIGHT,Keys.LEFT]
for i in range(500):
	elem.send_keys(sample(keys_options,1))
	sleep(0.1)


