import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

@pytest.fixture(autouse=True)
def driver():
   driver = webdriver.Chrome('E:\chromedriver.exe')
   # Устанавливаем неявное ожидание
   driver.implicitly_wait(10)
   # Переходим на страницу авторизации
   driver.get('http://petfriends.skillfactory.ru/login')
   # Вводим email
   WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'email'))).send_keys('vakalov.92.20.12@gmail.com')
   # Вводим пароль
   WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'pass'))).send_keys('exat2012')
   # Нажимаем на кнопку входа в аккаунт
   WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]'))).click()
   # Переходим в "Мои питомцы"
   WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME,'nav-link'))).click()

   yield

   driver.quit()