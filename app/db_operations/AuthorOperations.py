from app.app import db
from app.models.Author import Author


def get_all_authors():
    return Author.query.all()


def get_author_from_db_by_name(name):
    return Author.query.filter_by(name=name).first()


def add_author_to_db(author):
    try:
        db.session.add(author)
        db.session.commit()
    except Exception as e:
        print(e)


def add_author_lists_to_db(authors):
    try:
        for author in authors:
            db.session.add(author)
        db.session.commit()
    except Exception as e:
        print(e)