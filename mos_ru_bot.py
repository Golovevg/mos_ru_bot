from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def login(login, password):
    driver = webdriver.Chrome()

    driver.get("https://www.mos.ru/pgu/ru/application/oiv/booking/#step_2")
    driver.implicitly_wait(10)

    login = login
    password = password

    login_field = driver.find_element(By.ID, "login")
    login_field.send_keys(login)
    driver.implicitly_wait(7)

    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys(password)
    driver.implicitly_wait(7)

    mos_ru_enter = driver.find_element(By.ID, "bind")
    mos_ru_enter.click()