from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver = "C:/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver)

driver.get("https://www.empireonline.com/movies/features/best-movies-2/")
m = []
all_movies = driver.find_elements(By.CSS_SELECTOR, "div h3")
for movie in all_movies:
    m.append(movie.text)
mo = m[::-1]

with open("movies123.txt", "w") as file:
    for o in mo:
        file.write(f"{o}\n")

driver.close()