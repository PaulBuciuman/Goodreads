from bs4 import BeautifulSoup as bs
import requests


def get_page_contents(url):
    r = requests.get(url)
    return bs(r.content, "lxml")


def get_last_page_counter(page):
    return int(page.find("a", {"class": "next_page"}).findPreviousSibling().text)