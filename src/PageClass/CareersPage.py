'''
Created on Mar 23, 2017

@author: Gouri
'''
from PageClass.FirefoxPage import FirefoxPage

class CareersPage(FirefoxPage):
    def __init__(self):
        print (self.driver)
        
    def carrersLinkClick(self):
        self.driver.find_element_by_xpath("//a[text()='Careers']").click()
        
    def contextClick(self):
        self.driver.find_element_by_id("button")
        
    def doubleclick(self):
        self.driver.find_element_by_name("signButton")
        
    def buttonclick(self):
        self.driver.find_element_by_id("enable")
