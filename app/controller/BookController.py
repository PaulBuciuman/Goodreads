from app.controller.AuthorController import get_author_from_author_page
from app.controller.Scrapers.Scraper import get_page_contents
from app.models.Book import Book
from app.db_operations.AuthorOperations import get_author_from_db_by_name, add_author_to_db
from app.db_operations.BookOperations import add_book_list_to_db


def get_book_ratings(soup):
    book_ratings = soup.find_all("span", {"class": "minirating"})
    rating_scores = []
    rating_counts = []
    for rating in book_ratings:
        *_, last = rating.strings #one of the books has a string before the rating value, it's tag having multiple texts.We extract the last one
        rating_scores.append(last.strip().split(" ")[0])
        rating_counts.append(rating.text.strip().split("— ")[1].split(" ")[0].replace(",",""))

    return rating_scores, rating_counts


def get_books(titles, authors, ratings, ratings_count, genre):
    books = []
    for i in range(0,len(ratings)):
        book = Book(titles[i], authors[i], ratings[i], ratings_count[i], 0, genre)
        books.append(book)
    return books


def get_book_titles(soup):
    book_titles = soup.find_all("a", {"class": "bookTitle"})
    titles = []
    for title in book_titles:
        titles.append(title.text.strip())
    return titles


def get_book_authors(soup):
    book_authors = soup.find_all("a", {"class": "authorName"})
    authors = []
    for author in book_authors:
        author_id = None
        try:
            author_id = get_author_from_db_by_name(author.text).id
        except Exception as e:
            author_page = get_page_contents(author.get("href"))
            try:
                author = get_author_from_author_page(author_page)
                add_author_to_db(author)
                author_id = get_author_from_db_by_name(author.name).id
            except Exception as e:
                print(e)
        authors.append(author_id)
    return authors


def add_books_from_page_to_db(page,li):
    titles = get_book_titles(page)
    authors = get_book_authors(page)
    rating_scores, rating_counts = get_book_ratings(page)
    try:
        add_book_list_to_db(get_books(titles, authors, rating_scores, rating_counts, li.find("a").text))
    except Exception as e:
        print(e)
