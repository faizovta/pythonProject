from selenium import webdriver
import time

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

link = "https://www.google.ru/"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    searchbox = browser.find_element(By.TAG_NAME, "input")
    searchbox.send_keys("Калькулятор")
    searchbox.submit()

    button1 = browser.find_element(By.CSS_SELECTOR, "[jsname='N10B9'] ").click()
    button2 = browser.find_element(By.CSS_SELECTOR, "[aria-label='умножение'] ").click()
    button3 = browser.find_element(By.CSS_SELECTOR, "[jsname='lVjWed'] ").click()
    button4 = browser.find_element(By.CSS_SELECTOR, "[aria-label='вычитание'] ").click()
    button5 = browser.find_element(By.CSS_SELECTOR, "[jsname='KN1kY'] ").click()
    button6 = browser.find_element(By.CSS_SELECTOR, "[aria-label='сложение'] ").click()
    button7 = browser.find_element(By.CSS_SELECTOR, "[jsname='N10B9'] ").click()
    button6 = browser.find_element(By.CSS_SELECTOR, "[aria-label='равно'] ").click()
finally:
    time.sleep(1)
    # закрываем браузер после всех манипуляций
    browser.quit()

