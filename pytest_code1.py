__author__ = 'Vishvesh Savant'
__author__ = 'Vishvesh Savant'
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

driver = webdriver.Firefox()
driver.get("http://www.seleniumframework.com/Practiceform/")
assert "Selenium Framework" in driver.title
driver.maximize_window()

def test_ClearText():                                                                #Enter in text box
   text_box_elem = driver.find_element_by_xpath("//textarea[@id='vfb-10']")
   text_box_elem.clear()
   text_box_elem.send_keys("Testing..")

def test_TextBox():                                                                 #Enter in Text
   text_elem = driver.find_element_by_xpath("//input[@id='vfb-9']")
   text_elem.clear()
   text_elem.send_keys("Testing Text")


"""a=ClearText()
b=TextBox()
c=CheckBox()
d=RadioButton()"""



