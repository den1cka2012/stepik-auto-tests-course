from selenium.webdriver.support.ui import Select
from selenium import webdriver
import math, time


try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element_by_id('num1')
    y = browser.find_element_by_id('num2')
    sum = int(x.text) + int(y.text)
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text(str(sum))
    btn = browser.find_element_by_class_name("btn")
    btn.click()

finally:
    time.sleep(10)
    browser.quit()