import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import WebDriverWait
# as EC принято называть для сокращения длинного "expected_conditions"
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from stepik_authorize import test_authorize



@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('id', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_input(browser, id):
    link=f"https://stepik.org/lesson/{id}/step/1"
    #link=f"https://stepik.org/lesson/236898/step/1"
    test_authorize(browser, link)
    wait = WebDriverWait(browser, 50)
    element = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "textarea")))
    answer = math.log(int(time.time()))
    big_input=browser.find_element(By.TAG_NAME, "textarea")
    time.sleep(1)
    big_input.send_keys(answer)
    button3=browser.find_element(By.CLASS_NAME, "submit-submission")
    time.sleep(1)
    button3.click()
    element2 = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "smart-hints__hint")))

    ok_text = browser.find_element(By.CLASS_NAME, "smart-hints__hint")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    text = ok_text.text
    time.sleep(1)

    assert text == "Correct!", \
        f"{text} - вместо 'Correct!'"  