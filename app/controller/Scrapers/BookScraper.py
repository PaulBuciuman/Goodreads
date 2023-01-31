import sys

from app.db_operations.BookOperations import add_book_list_to_db
from bs4 import BeautifulSoup as bs
from app.controller.BookController import get_book_ratings,get_books,get_book_titles,get_book_authors,add_books_from_page_to_db
from app.controller.Scrapers.Scraper import get_page_contents,get_last_page_counter

import requests


BASE_URL = "https://www.goodreads.com"


def get_list_of_all_genres(soup):
    ul_wrapper = soup.find_all("ul", {"class": "listTagsTwoColumn"})
    all_lists = []
    for tag in ul_wrapper:
        list = tag.find_all("li")
        all_lists.extend(list)
    return all_lists


def get_books_data():
    r = requests.get("https://www.goodreads.com/list?ref=nav_brws_lists")
    first_page = bs(r.content, "lxml")
    all_lists = get_list_of_all_genres(first_page)
    for li in all_lists:
        page = get_page_contents(BASE_URL+li.find("a").get('href'))
        last_page_counter = get_last_page_counter(page)
        for list_index in range(0,last_page_counter):
            page = get_page_contents(BASE_URL + li.find("a").get('href')+"?page="+str(list_index+1))
            links = page.find_all("a", {"class": "listTitle"})
            for link in links:
                page = get_page_contents(BASE_URL + link.get('href'))
                page_counter = get_last_page_counter(page)
                for book_pages_index in range(0, page_counter):
                    page = get_page_contents(BASE_URL + link.get('href') + "?page=" + str(book_pages_index + 1))
                    add_books_from_page_to_db(page,li)

