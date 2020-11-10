class Info():
    author = "Anonymous"

    def __init__(self, game_title, game_description):
        self.title = game_title
        self.description = game_description

    def welcome(self):
        print("Welcome to " + self.title)
        print(self.description)
        print("--------------------")

    @staticmethod
    def info():
        print("Developed in Python with OOP")
        print("--------------------")

    @classmethod
    def credits(cls):
        print("Thank you for playing")
        print("Created by " + cls.author)
