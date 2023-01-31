from app.controller.Scrapers.Scraper import get_page_contents
from app.models.Author import Author

BASE_URL = "https://www.goodreads.com"


def reviews_and_followers_count(div):
    reviews_count = int(div.find_next("div", {"class": "right greyText"}).text.strip().split(" ")[0].replace(",",""))
    followers_count = int(div.find_next("div", {"class": "right greyText"}).text.strip().split("\n")[2].split(" ")[-2].replace(",",""))
    return reviews_count, followers_count


def get_avg_rating(page):
    return page.find("span", {"class": "average"}).text


def get_ratings_count(page):
    return page.find("span", {"class": "votes"}).text.strip().replace(",","")


def get_author_from_author_page(author_page):
    author_details = author_page.find("div", {"class": "hreview-aggregate"})
    name = author_details.find("span", {"class": "item fn"}).text.strip()
    books_count = int(author_details.find_next("a").text.strip().split(" ")[0].replace(",", ""))
    avg_rating = author_details.find("span", {"class": "average"}).text.strip()
    ratings_count = int(author_details.find("span", {"class": "votes"}).text.strip().replace(",", ""))
    reviews_count = int(author_details.find("span", {"class": "count"}).text.strip().replace(",", ""))
    try:
        followers_count = int(author_page.find("h2", {"class": "brownBackground"}).text.strip().split("(")[1].split(")")[0].replace(",", ""))
    except:
        followers_count = 0
    return Author(name, books_count, followers_count, avg_rating, ratings_count, reviews_count)


def get_author_from_author_list(div):
    name = div.find_next("a", {"class": "bookAuthorProfile__name"}).text
    books_count = int(div.find_all("a")[3].text.split(" ")[0]) + 1
    reviews_count, followers_count = reviews_and_followers_count(div)
    author_page = get_page_contents(BASE_URL + div.find("a").get('href'))
    avg_rating = get_avg_rating(author_page)
    ratings_count = get_ratings_count(author_page)
    return Author(name, books_count, followers_count, avg_rating, ratings_count, reviews_count)