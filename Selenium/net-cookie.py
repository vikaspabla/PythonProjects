from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

chrome_driver_path = "C:/chromedriver.exe"

service = Service(chrome_driver_path)

driver = webdriver.Chrome(service=service)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

timeout = time.time() + 5
game_over = time.time() + 5 * 60

click_cookie = driver.find_element(By.XPATH, '//*[@id="cookie"]')

while True:
    click_cookie.click()
    if time.time() > timeout:

        try:
            items = driver.find_elements(By.CSS_SELECTOR, "#store div")
            item_ids = [item.get_attribute("id") for item in items]
            item_ids.reverse()
            click_cookie = driver.find_element('//*[@id="cookie"')
        except:
            pass
        for i in item_ids:
            try:
                driver.find_element(By.CSS_SELECTOR, f"#{i}").click()
            except:
                pass
        timeout = timeout + 5
    if time.time() > game_over:
        cookies_seconds = driver.find_element(By.XPATH, '//*[@id="cps"]')
        print(cookies_seconds.text)

        break