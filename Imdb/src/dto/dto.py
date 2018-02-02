

import json


class BaseDTO(object):
    def dict_for_json(self):
        return self.__dict__

    def to_json(self):
        return json.dumps(self.__dict__)

class MovieDTO(BaseDTO):
    def __init__(self, movie_id, popularity, director, imdb_score, movie_name,genre):
        self.movie_id= movie_id
        self.popularity = popularity
        self.director = director
        self.imdb_score = imdb_score
        self.movie_name = movie_name
        self.genre = genre
