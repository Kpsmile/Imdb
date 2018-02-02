import json
class DeleteMovieService(object):
    def __init__(self, operations):
        self.operations =  operations

    def delete_movie(self, movie_id):
        try:
            self.operations.delete_movie(movie_id)

            return 200, json.dumps('Movie is deleted')

        except Exception as exception:
            raise exception
        except Exception as exception:
            print(exception)