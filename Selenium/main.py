from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver = "C:/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver)

# driver.get("https://www.amazon.com/Nintendo-Switch-Neon-Blue-Joy%E2%80%91/dp/B07VGRJDFY/ref=lp_16225016011_1_4?th=1")
# price = driver.find_element(By.ID, "price_inside_buybox")
# print(price.text)
# driver.close()

driver.get("https://www.python.org/")

dates = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")

events = {}

for n in range(len(dates)):
    events[n] = {
        "time": dates[n].text,
        "name": names[n].text,
    }

print(events)

driver.close()
