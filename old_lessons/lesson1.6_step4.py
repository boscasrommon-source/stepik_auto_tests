from selenium import webdriver
import requests


proxies = {'http': 'localhost:8080'}
# Создаем экземпляр веб-драйвера для Chrome
driver = webdriver.Chrome()

# Открываем веб-страницу
driver.get('https://www.example.com', proxies=proxies)

# Выводим заголовок страницы в консоль
print(driver.title)

# Закрываем браузер
driver.quit()