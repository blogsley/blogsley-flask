from blogsley_flask import db
from blogsley_flask.models.users import User
from blogsley_flask.models.blog import Post

users = User.query.all()
for u in users:
  db.session.delete(u)
posts = Post.query.all()
for p in posts:
  db.session.delete(p)
db.session.commit()