from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
browser = webdriver.Firefox()
browser.get('https://gabrielecirulli.github.io/2048/')
time.sleep(5)
html = browser.find_element_by_tag_name('html')
count = 0
while True:
	for x in range(4):
		html.send_keys(Keys.UP)
	html.send_keys(Keys.LEFT)
	html.send_keys(Keys.UP)
	html.send_keys(Keys.RIGHT)
	for x in range(4):
		html.send_keys(Keys.UP)
	html.send_keys(Keys.RIGHT)
	html.send_keys(Keys.UP)
	html.send_keys(Keys.LEFT)
	count +=1
	if count % 200 == 0:
		html.send_keys(Keys.DOWN)
	'''
	for x in range(4):
		html.send_keys(Keys.RIGHT)
		html.send_keys(Keys.UP)
	for y in range(2):
		html.send_keys(Keys.UP)
	for x in range(2):
		html.send_keys(Keys.RIGHT)
	for z in range(2):
		html.send_keys(Keys.LEFT)
		html.send_keys(Keys.UP)
	'''