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
