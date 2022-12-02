import requests
from bs4 import BeautifulSoup
response = requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
webpage = response.text
soup = BeautifulSoup(webpage, "html.parser")
movies_list = []
all_movies = soup.find_all(name="h3", class_="title")
for movie in all_movies:
    movies_list.append(movie.text)
    movies_list.reverse()
with open("movies.txt", mode="w") as file:
    for movie in movies_list:
        file.write(f"{movie}")
