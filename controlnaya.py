# задача номер 10
from datetime import datetime


class Post:
    def __init__(self, author, message):
        self.author = author
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.likes = 0
        self.message = message
        self.comments = []
        self.swear_words = 0

    def add_like(self):
        self.likes += 1

    def reset_swear_words(self):
        self.swear_words = 0


post = Post("Каплан", "Привет я каплан")

print(post.swear_words)

post.reset_swear_words()

print(post.swear_words)

print(post.likes)

post.add_like()

print(post.likes)
