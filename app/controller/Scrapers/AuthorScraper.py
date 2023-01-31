from bs4 import BeautifulSoup as bs
from app.controller.AuthorController import reviews_and_followers_count, get_avg_rating, get_ratings_count, \
    get_author_from_author_list
from app.models.Author import Author
from app.controller.Scrapers.Scraper import get_last_page_counter,get_page_contents
from app.db_operations.AuthorOperations import add_author_to_db

BASE_URL = "https://www.goodreads.com"


def get_authors_data():
    first_page = get_page_contents(BASE_URL+"/author/on_goodreads")
    last_page_counter = get_last_page_counter(first_page)
    for index in range(0, last_page_counter):
        page = get_page_contents(BASE_URL+"/author/on_goodreads"+"?page="+str(index+1))
        author_divs = page.find_all("div", {"class": "elementList bookAuthorProfile u-paddingBottomSmall u-paddingTopSmall"})
        for div in author_divs:
            try:
                add_author_to_db(get_author_from_author_list(div))
            except Exception as e:
                print(e)

