import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By


link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)


x_element = browser.find_element(By.CSS_SELECTOR,'#num1')
y_element = browser.find_element(By.CSS_SELECTOR,'#num2')
x = x_element.text
y = y_element.text
z = int(x) + int(y)
value = str(z)

from selenium.webdriver.support.ui import Select
select = Select(browser.find_element(By.TAG_NAME, "select"))
select.select_by_visible_text(value)

button = browser.find_element(By.TAG_NAME,"button")
button.click()


time.sleep(30)

