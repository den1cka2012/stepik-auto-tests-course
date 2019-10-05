from selenium import webdriver
import math, time, os

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    option1 = browser.find_element_by_css_selector("input[name='firstname']")
    option1.send_keys('Stepnyak')
    option2 = browser.find_element_by_css_selector("input[name='lastname']")
    option2.send_keys('Kravchinsky')
    option3 = browser.find_element_by_css_selector("input[name='email']")
    option3.send_keys('skrav@mail.com')
    option4 = browser.find_element_by_css_selector("input[name='file']")
    option4.send_keys(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'file.txt'))

    browser.find_element_by_class_name("btn").click()


finally:
    time.sleep(10)
    browser.quit()