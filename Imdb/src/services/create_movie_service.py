import json
class CreateMovieService(object):
    def __init__(self, operations):
        self.operations =  operations

    def create_movie(self, movie_data_model):
        try:
            movie_id = self.operations.save_movie(movie_data_model)
            if movie_id:
                return 200, json.dumps('Newly Movie Created')
            else:
                return 404, json.dumps("Movie not created")

        except Exception as exception:
            raise exception