from app import db

from models import BlogPost

# create database
db.create_all()

# insert
db.session.add(BlogPost("Whee", "So Fun!"))
db.session.add(BlogPost("Boo", "Not Fun!"))

# commit
db.session.commit()