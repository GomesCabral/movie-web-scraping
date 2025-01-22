# Movie List Scraper

This Python script scrapes a list of the best movies from an article on **Empire Online** using the **BeautifulSoup** library. The list of movies is extracted from the webpage, reversed, and then saved to a text file (`movie.txt`).

## Features
- **Web Scraping**: The script scrapes a webpage that contains a list of movies.
- **Movie Extraction**: Extracts movie titles from specific HTML elements.
- **Data Reversal**: Reverses the order of the movie list before saving.
- **File Output**: Saves the reversed movie list into a text file.

## Technologies Used
- **Python**: The programming language used for this script.
- **BeautifulSoup**: A Python library for parsing HTML and XML documents.
- **Requests**: A Python library to send HTTP requests and retrieve web pages.

## Requirements
Before running the script, make sure you have the following libraries installed:

```bash
pip install beautifulsoup4
pip install requests
````

Usage
Clone this repository to your local machine:
  git clone https://github.com/your-username/movie-list-scraper.git
  cd movie-list-scraper
  cd movie-list-scraper
  python movie_scraper.py

After the script runs, check the generated movie.txt file, which contains the list of movie titles in reversed order.

How the Script Works
The script sends a request to the URL of the Empire Online article on the best movies.
It retrieves the HTML of the page using requests.
Using BeautifulSoup, it parses the HTML and extracts all the movie titles located in <h3> elements with the class title.
The list of movies is reversed.
The reversed list of movie titles is saved into a text file called movie.txt.

Movie Title 100
Movie Title 99
Movie Title 98
...
Movie Title 1
