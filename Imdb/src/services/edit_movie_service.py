import json
class EditMovieService(object):
    def __init__(self, operations):
        self.operations =  operations

    def edit_movie(self, movie_id, popularity=None, director=None, imdb_score=None, movie_name=None):
        try:
            movie = self.operations.edit_movies(movie_id,popularity, director, imdb_score, movie_name)
            if movie_id == movie[0]:
                response_dictionary = {"movie_id": movie_id}
                return 200, json.dumps(response_dictionary )
            else:
                return 404, json.dumps("Movie not updated")

        except Exception as exception:
            raise exception