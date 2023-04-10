from . import db
class Movies(db.Model):
    __tablename__ = 'movies'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    description = db.Column(db.Text)
    poster = db.Column(db.String(255))
    created_at = db.Column(db.DateTime)

    def __init__(self, id, title, description, poster, created_at):
        self.id = id
        self.title = title
        self.description = description
        self.poster = poster
        self.created_at = created_at

    def __repr__(self):
        return f'<Movie {self.id}>'