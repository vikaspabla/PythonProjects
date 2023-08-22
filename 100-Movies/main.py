from bs4 import BeautifulSoup

import requests



response = requests.get("https://www.hollywoodreporter.com/lists/100-best-films-ever-hollywood-favorites-818512/the-seven-samurai/")
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")

all_movies = soup.find_all(name="h2", class_="c-gallery-vertical-featured-image__title")

print(all_movies)
#
# article_texts = [movie.getText() for movie in all_movies]
#
# print(article_texts)
