import pytest
import time
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_start_for_difr_language(browser):
    browser.get(link)
    browser.implicitly_wait(5)
    assert (len(browser.find_elements_by_class_name("btn-add-to-basket")) > 0), "Кнопка 'В корзину' не найдена"
    #time.sleep(30)