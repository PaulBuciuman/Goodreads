from app.app import db

class Book(db.Model):
    def __init__(self,name,author_id,rating_score,rating_count,reviews_count,genre):
        self.name=name
        self.author_id=author_id
        self.rating_score=rating_score
        self.rating_count=rating_count
        self.reviews_count=reviews_count
        self.genre=genre

    __tablename__ = 'book'
    id = db.Column(db.Integer, primary_key=True)
    name =  db.Column(db.String(200), nullable=False)
    author_id =  db.Column(db.Integer, db.ForeignKey('author.id'))
    rating_score =  db.Column(db.Float)
    rating_count =  db.Column(db.Integer)
    reviews_count =  db.Column(db.Integer)
    genre = db.Column(db.String(100))

    def __repr__(self):
        return f'<Book {self.name}, By: {self.author_id}, Average Rating: {self.rating_score}, Total Ratings: {self.rating_count}, Total Reviews: {self.reviews_count}>'

