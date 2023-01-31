from app.app import db


class Author(db.Model):
    __tablename__ = "author"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    books_count = db.Column(db.Integer)
    followers_count = db.Column(db.Integer)
    avg_rating = db.Column(db.Float)
    ratings_count = db.Column(db.Integer)
    reviews_count = db.Column(db.Integer)
    books = db.relationship('Book', backref='post')

    def __init__(self,name,books_count,followers_count,avg_rating,ratings_count,reviews_count):
        self.name=name
        self.books_count=books_count
        self.followers_count = followers_count
        self.avg_rating=avg_rating
        self.ratings_count=ratings_count
        self.reviews_count=reviews_count

    def __repr__(self):
        return f'<Author {self.name}, Total Books Written: {self.books_count}, Average Rating: {self.avg_rating}, Followers: {self.followers_count}>'