import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


def test_authorize(browser, link):
    x='boscas@yandex.ru'
    y='961mt87rk'
    browser.get(link)
    time.sleep(3)
    button1=browser.find_element(By.CLASS_NAME, "ember-view.navbar__auth.navbar__auth_login.st-link.st-link_style_button")
    button1.click()
    time.sleep(1)
    input1 = browser.find_element(By.ID, 'id_login_email')
    input1.send_keys(x)
    input2 = browser.find_element(By.ID, 'id_login_password')
    input2.send_keys(y)
    button2=browser.find_element(By.CLASS_NAME, "sign-form__btn.button_with-loader")
    button2.click()
    time.sleep(2)