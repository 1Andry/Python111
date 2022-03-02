import pickle
import os.path


class Film:
    def __init__(self, title, genre, producer, year, movie_duration, studio, actors):
        self.title = title
        self.genre = genre
        self.producer = producer
        self.year = year
        self.movie_duration = movie_duration
        self.studio = studio
        self.actors = actors

    def __str__(self):
        return f"{self.title} {self.producer}"


class FilmModel:
    def __init__(self):
        self.db_films = "db.txt"
        self.film = self.load_data()

    def add_film(self, dict_film):
        film = Film(*dict_film.values())
        self.film[film.title] = film

    def get_all_films(self):
        return self.film.values()

    def get_single_film(self, user_title):
        film = self.film[user_title]
        dict_film = {
            "название": film.title,
            "жанр": film.genre,
            "режиссер": film.producer,
            "год выпуска": film.year,
            "длительность": film.movie_duration,
            "студия": film.studio,
            "актеры": film.actors
        }
        return dict_film

    def remove_film(self, title_film):
        return self.film.pop(title_film)

    def load_data(self):
        if os.path.exists(self.db_films):
            with open(self.db_films, "rb") as f:
                return pickle.load(f)

        else:
            return dict()

    def save_data(self):
        with open(self.db_films, "wb") as f:
            pickle.dump(self.film, f)
