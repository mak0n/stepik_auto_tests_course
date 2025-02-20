from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    link = "https://suninjuly.github.io/redirect_accept.html"
    browser.get(link)

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    #confirm = browser.switch_to.alert
    #confirm.accept()

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    print(x)

    result = calc(x)
    print(result)

    click1 = browser.find_element(By.ID, ("answer"))
    click1.send_keys(result)
    #browser.find_element(By.ID, "answer").send_keys(result) Короче и круче, но пока по методичке курса

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
