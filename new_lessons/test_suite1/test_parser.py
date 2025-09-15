link = "http://selenium1py.pythonanywhere.com/"


def test_guest_should_see_login_link(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")
    parser.addoption('--browser_name', action='store', default="chrome",
                 help="Choose browser: chrome or firefox")