from selenium import webdriver

path = 'E:\anaconda\geckodriver.exe' #import
brower = webdriver.Firefox()
brower.get('http://localhost:8000')

assert 'Django' in brower.title