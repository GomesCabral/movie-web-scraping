from bs4 import BeautifulSoup
import requests

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
web_page = response.text
soup = BeautifulSoup(web_page, 'html.parser')

all_movies = soup.find_all('h3', class_='title')
#print(all_movies)

movie_title = [movie.getText() for movie in all_movies]
order_movies = movie_title[::-1]
#mesma coisa--> para verter
#for n in range(len(movie_title) -1, -1, -1):
    #print(movie_title[n])
#print(order_movies)

with open('movie.txt', 'w', encoding="utf8") as f:
    for movie in order_movies:
        f.write(f'{movie}\n')