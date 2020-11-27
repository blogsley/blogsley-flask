from blogsley_flask import db
from blogsley_flask.models.users import User
from blogsley_flask.models.blog import Post

users = User.query.all()
print(users)

posts = Post.query.all()
for p in posts:
  print(p.id, p.author.username, p.body)