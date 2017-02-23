from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

browser = webdriver.Firefox(firefox_binary=FirefoxBinary(
    firefox_path='/home/carl/git/testing_goat/firefox/firefox'
))

browser.get('http://localhost:8001')

assert 'Django' in browser.title
