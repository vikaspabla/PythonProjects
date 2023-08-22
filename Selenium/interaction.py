from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver = "C:/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

# n = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
#
# n.click()

portals = driver.find_element(By.NAME, "search")
portals.send_keys("Hello")
portals.send_keys(Keys.ENTER)
