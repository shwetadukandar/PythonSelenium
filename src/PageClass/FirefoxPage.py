'''
Created on Mar 23, 2017

@author: Gouri
'''
from selenium import webdriver

class FirefoxPage(object):
    
    driver=webdriver.Firefox()
    driver.get("https://www.Amazon.com")
    #driver.quit()
   
    def __init__(self):
        print (self.driver)
      
        