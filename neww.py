from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
    input1.send_keys('John')
    input2 = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
    input2.send_keys('John')
    input3 = browser.find_element(By.CSS_SELECTOR, "[name='email']")
    input3.send_keys('John')

    input4 = browser.find_element(By.CSS_SELECTOR, "#file")

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'new.txt')  # добавляем к этому пути имя файла
    input4.send_keys(file_path)

    option1 = browser.find_element(By.CSS_SELECTOR, ".btn")
    option1.click()

finally:
    time.sleep(5)
    browser.quit()