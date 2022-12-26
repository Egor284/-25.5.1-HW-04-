
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_allpets(driver): # Проверяем что присутствуют все питомцы.

   # Устанавливаем явное ожидание
   WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//th[@scope='row']/img")))
   # Сохраняем в переменную pets питомцев отображенных на странице
   pets = driver.find_elements(By.XPATH,"//th[@scope='row']/img")
   # Устанавливаем явное ожидание
   WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='.col-sm-4 left']")))
   # Сохраняем в переменную account данные пользователя
   account = driver.find_elements(By.XPATH,"//div[@class='.col-sm-4 left']")
   # Получаем количество питомцев из данных пользователя
   all_pets = account[0].text.split('\n')
   all_pets = all_pets[1].split(' ')
   all_pets = int(all_pets[1])
   # Проверяем что количество питомцев из данных пользователя равно колличеству отображенных питомцев
   assert all_pets == len(pets)

def test_photopets(driver): #проверяем наличие фото у питомцев

   # Устанавливаем явное ожидание
   WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//th[@scope='row']/img")))
   # Сохраняем в переменную pets питомцев отображенных на странице
   pets = driver.find_elements(By.XPATH,"//th[@scope='row']/img")
   # Сохраняем в переменную photos питомцев,c фото
   photos = 0
   for i in range(len(pets)):
      if pets[i].get_attribute('src') != '':
         photos += 1
   # Сохраняем в переменную account данные пользователя
   account = driver.find_elements(By.XPATH,"//div[@class='.col-sm-4 left']")
   # Получаем количество питомцев из данных пользователя
   all_pets = account[0].text.split('\n')
   all_pets = all_pets[1].split(' ')
   all_pets = int(all_pets[1])
   # Проверяем что хотя бы у половины питомцев есть фото
   assert photos >= all_pets // 2

def test_name(driver): #проверяем наличие имени,возраста,породы

   # Устанавливаем явное ожидание
   WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//td[@class='smart_cell']/preceding-sibling::td")))
   # Сохраняем в переменную datapets данные о питомцах
   datapets = driver.find_elements(By.XPATH,"//td[@class='smart_cell']/preceding-sibling::td")
   # Перебираем данные из datapets и сравниваем их с ожидаемым результатом
   for i in range(len(datapets)):
      assert datapets[i].text != ''

def test_variousnames(driver): #проверяем имена питомцев

   # Устанавливаем явное ожидание
   WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//td[@class='smart_cell']/preceding-sibling::td[3]")))
   # Сохраняем в переменную name информацию с именами питомцев
   name = driver.find_elements(By.XPATH,"//td[@class='smart_cell']/preceding-sibling::td[3]")
   # Перебираем имена и добавляем их в список names
   names = []
   for i in range(len(name)):
      names.append(name[i].text)
   # преобразуем список с именами в множество и сравниваем его длину с длиной списка names
   assert len(set(names)) == len(names)

def test_duplicate_pets(driver): #проверяем что нет повторяющихся питомцев

   # Устанавливаем явное ожидание
   WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//td[@class='smart_cell']/preceding-sibling::td[3]")))
   # Сохраняем в переменную name информацию с именами питомцев
   name = driver.find_elements(By.XPATH,"//td[@class='smart_cell']/preceding-sibling::td[3]")
   # Устанавливаем явное ожидание
   WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//td[@class='smart_cell']/preceding-sibling::td[2]")))
   # Сохраняем в переменную breed информацию с породами питомцев
   breed = driver.find_elements(By.XPATH,"//td[@class='smart_cell']/preceding-sibling::td[2]")
   # Устанавливаем явное ожидание
   WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//td[@class='smart_cell']/preceding-sibling::td[1]")))
   # Сохраняем в переменную age информацию с возрастом питомцев
   age = driver.find_elements(By.XPATH,"//td[@class='smart_cell']/preceding-sibling::td[1]")
   # Перебираем имена и добавляем их в список names
   names = []
   for i in range(len(name)):
      names.append(name[i].text)
   # Перебираем породы и добавляем их в список breeds
   breeds = []
   for i in range(len(breed)):
      breeds.append(breed[i].text)
   # Перебираем возраст и добавляем их в список ages
   ages = []
   for i in range(len(age)):
      ages.append(age[i].text)
   # Перебираем имена, породы и возраст, и добавляем их в список datapets
   datapets = []
   for (a, b, c) in zip(names, breeds, ages):
      datapets.append(a+b+c)
   # преобразуем список с именами в множество и сравниваем его длину с длиной списка datapets
   assert len(set(datapets)) == len(datapets)
