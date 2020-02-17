import time
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def init_driver():
    driver = Firefox()
    driver.wait = WebDriverWait(driver, 5)
    return  driver


def lookup(driver, query):
    driver.get('https://www.yandex.ru')
    try:
        box = driver.wait.until(EC.presence_of_element_located(
            (By.ID, 'text'),
        ))
        print(12)
        button = driver.wait.until(EC.presence_of_element_located(
            (By.CLASS_NAME, 'suggest2-form__button')
        ))
        box.send_keys(query)
        button.click()
    except TimeoutException:
        print('Box or Button didnt find')
    html = driver.page_source
    with open('index.html', 'w') as f:
        f.write(html)

driver = init_driver()
lookup(driver, 'i love beer')
time.sleep(5)
driver.quit()