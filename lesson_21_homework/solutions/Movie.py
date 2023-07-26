class Movie:

    def __init__(self, name, genre, rating, year):
        self.name = name
        self.genre = genre
        self.rating = rating
        self.year = year

    def __str__(self) -> str:
        return f"{self.genre} din {self.year} numit {self.name} cu {self.rating} puncte."
