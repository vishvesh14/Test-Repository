__author__ = 'Vishvesh Savant'
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

driver = webdriver.Firefox()
driver.get("http://www.seleniumframework.com/Practiceform/")
assert "Selenium Framework" in driver.title
driver.maximize_window()

def ClearText():                                                                #Enter in text box
   text_box_elem = driver.find_element_by_xpath("//textarea[@id='vfb-10']")
   text_box_elem.clear()
   text_box_elem.send_keys("Testing..")

def TextBox():                                                                 #Enter in Text
   text_elem = driver.find_element_by_xpath("//input[@id='vfb-9']")
   text_elem.clear()
   text_elem.send_keys("Testing Text")

def CheckBox():
    checkboxes=[]
    checkboxes=driver.find_elements_by_xpath("//input[@name='vfb-6[]']")
    for check in checkboxes:
        check.click()

def RadioButton():
    radiobutton = driver.find_elements_by_xpath("//input[@type='radio']")
    for radio in radiobutton:
        radio.click()
    time.sleep(30)

a=ClearText()
b=TextBox()
c=CheckBox()
d=RadioButton()



