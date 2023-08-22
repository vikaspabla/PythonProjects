from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver = "C:/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver)

driver.get("https://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("pabla")

last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("vikas")

email = driver.find_element(By.NAME, "email")
email.send_keys("tattu@lindi.com")

button = driver.find_element(By.CSS_SELECTOR, "form button")
button.click()