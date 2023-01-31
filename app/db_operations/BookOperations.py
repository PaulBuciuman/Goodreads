from app.app import db
from app.models.Book import Book


def get_all_books():
    return Book.query.all()


def get_book_from_db_by_name(name):
    return Book.query.filter_by(name=name).first()


def add_book_to_db(book):
    try:
        db.session.add(book)
        db.session.commit()
    except Exception as e:
        print(e)


def add_book_list_to_db(books):
    try:
        for book in books:
            db.session.add(book)
        db.session.commit()
    except Exception as e:
        print(e)

