import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class Test_form(unittest.TestCase):
    def test_regform1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        # Ваш код, который заполняет обязательные поля
        inputs = browser.find_elements(By.CSS_SELECTOR, '[required]')
        for i in inputs:
            i.send_keys('text')
        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # находим элемент, содержащий текст используя ожидание
        welcome_text_elt = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        true_text = "Congratulations! You have successfully registered!"
        self.assertEqual(true_text, welcome_text, 'reg is failed')

    def test_regform2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        # Ваш код, который заполняет обязательные поля
        inputs = browser.find_elements(By.CSS_SELECTOR, '[required]')
        for i in inputs:
            i.send_keys('text')
        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # находим элемент, содержащий текст используя ожидание
        welcome_text_elt = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        true_text = "Congratulations! You have successfully registered!"
        self.assertEqual(true_text, welcome_text, 'reg is failed')


if __name__ == "__main__":
    unittest.main()
