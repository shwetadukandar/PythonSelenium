'''
Created on Mar 30, 2017

@author: Gouri
'''
from selenium import webdriver
import time
if __name__ == '__main__':
    driver=webdriver.Firefox()
    driver.get("https://www.Twitter.com")
   
    time.sleep(4)
   
    driver.find_element_by_xpath("//a[text()='Log in']").click()
   #email
    driver.find_element_by_name("session[username_or_email]").send_keys("rachappahalinge@gmail.com")
   #password
    driver.find_element_by_name("session[password]").send_keys("rach222")
   #loginclick
    driver.find_element_by_xpath("//input[@class='submit btn primary-btn js-submit']").click()
    time.sleep(3)
    #language
    driver.find_element_by_xpath("//small[text()='Language:']").click()
    #english
    driver.find_element_by_xpath("//a[text()='Svenska']").click()
    