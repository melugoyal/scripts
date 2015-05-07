# script to automate submitting code to pastebin
# takes any number of file names as parameters and uses phantomjs to submit the code to pastebin and then prints out the pastebin url

import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
files = sys.argv[1:len(sys.argv)]
browser = webdriver.PhantomJS()
file_ext = {}
file_ext['py'] = '42'
file_ext['cpp'] = '13'
file_ext['c'] = '9'
file_ext['html'] = '25'
file_ext['js'] = '28'
file_ext['java'] = '27'
file_ext['rb'] = '45'
file_ext['scm'] = '46'
file_ext['R'] = '188'

for filename in files:
	browser.get('http://pastebin.com')
	f = open(filename, 'r')
	browser.find_element_by_id('paste_code').send_keys(f.read())
	ext = file_ext.get(filename[filename.index('.')+1:])
	if ext is not None:
		Select(browser.find_element_by_name('paste_format')).select_by_value(ext)
	Select(browser.find_element_by_name('paste_private')).select_by_value('1')
	browser.find_element_by_name('paste_name').send_keys(filename)
	browser.find_element_by_name('submit').click()
	print browser.current_url
browser.close()
