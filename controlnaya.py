# задача номер 10
from datetime import datetime


class Post:
    def __init__(self, author, message):
        self.author = author
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.likes = 0
        self.message = message
        self.comments = []

    def add_like(self):
        self.likes += 1


post = Post("Каплан", "Привет я каплан")

print(post.likes)

post.add_like()

print(post.likes)
