from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class fact(db.Model):
    __tablename__ = "facts"

    id = db.Column(db.Integer, primary_key = True)
    submitter = db.Column(db.String(250))
    face = db.Column(db.Text)