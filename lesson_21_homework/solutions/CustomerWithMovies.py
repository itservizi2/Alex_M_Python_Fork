from datetime import datetime, date

from lesson_21_homework.solutions.Movie import Movie


class CustomerWithMovies:

    def __init__(self,
                 first_name: str,
                 last_name: str,
                 date_of_birth: datetime,
                 movies: list = None
                 ):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.movies = movies or []

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_age(self):
        today = date.today()
        birth_date = self.date_of_birth
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        return age

    def __str__(self):
        movie_strings = ", ".join([str(movie) for movie in self.movies])
        if self.movies:
            nr_de_filme = f'un film:' if len(self.movies) == 1 else f"{len(self.movies)} filme:"
        else:
            nr_de_filme = "nici un film."
        return f"{self.full_name()} varsta {self.get_age()}, ce are {nr_de_filme} {movie_strings}"

    def buy_a_movie(self, movie):
        self.movies.append(movie)

    def give_away_movies(self, movie):
        self.movies.remove(movie)


if __name__ == '__main__':
    m1 = Movie("Fast and furious 12", "Action", "4/10", 2023)
    m2 = Movie("Avengers 5", "Action", "?/10", 2025)
    m3 = Movie("Hachikō", "Drama", "10/10", 2009)
    c = CustomerWithMovies(
        'Marius',
        "Tricolici",
        datetime(2022, 9, 30),
        []
    )
    c.buy_a_movie(m1)
    c.buy_a_movie(m2)
    c.buy_a_movie(m3)
    c.give_away_movies(m1)
    print(m1)
    print(m2)
    print(m3)
    print(c)
