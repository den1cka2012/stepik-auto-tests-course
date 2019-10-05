from selenium import webdriver
import math, time, os

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element_by_class_name("btn").click()
    browser.switch_to.alert.accept()
    x = browser.find_element_by_id('input_value')
    y = calc(x.text)
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(y)
    browser.find_element_by_class_name("btn").click()



finally:
    time.sleep(10)
    browser.quit()