from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver = "C:/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver)

driver.get("https://knowyourmeme.com/memes")

m= []
test_meme = driver.find_elements(By.CSS_SELECTOR, "title")
print(test_meme.text)

for n in test_meme:
    m.append(n.text)

with open("memes.txt", "w") as file:
    for o in m:
        file.write(f"{o}\n")

driver.close()

