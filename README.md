# Movie Title Scraper

This Python script utilizes BeautifulSoup and Requests libraries to scrape movie titles from a webpage and save them in a text file.

## Description

The code accesses a specific URL (`https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/`) using the `requests` library. Then, it uses `BeautifulSoup` to parse the HTML content and find all movie titles under the `<h3>` tag with the class `title`. The script retrieves the movie titles, reverses their order, and saves them into a text file named `movie.txt`.

## How to Use

1. Ensure you have Python installed.
2. Install the necessary libraries by running:
   ```bash
   pip install beautifulsoup4 requests

1. Run the Python script movie_title_scraper.py.
   python movie_title_scraper.py
2. After execution, the script will generate a file named movie.txt containing a list of movie titles scraped from the specified URL.

Important Note
Ensure that you have proper permissions to scrape content from the website in accordance with their terms of service and legal constraints.
Libraries Used
BeautifulSoup
Requests
Author
Gomes Cabral
