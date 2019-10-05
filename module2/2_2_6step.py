from selenium import webdriver
import math, time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    x = browser.find_element_by_id('input_value')
    y = calc(x.text)
    btn = browser.find_element_by_class_name("btn")
    browser.execute_script("window.scrollBy(0, 100);")
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(y)
    option1 = browser.find_element_by_css_selector("[for='robotCheckbox']")
    option1.click()
    option2 = browser.find_element_by_css_selector("[for='robotsRule']")
    option2.click()
    btn.click()

finally:
    time.sleep(10)
    browser.quit()