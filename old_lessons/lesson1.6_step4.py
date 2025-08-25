from selenium import webdriver

# Создаем экземпляр веб-драйвера для Chrome
driver = webdriver.Chrome()

# Открываем веб-страницу
driver.get('https://www.example.com')

# Выводим заголовок страницы в консоль
print(driver.title)

# Закрываем браузер
driver.quit()