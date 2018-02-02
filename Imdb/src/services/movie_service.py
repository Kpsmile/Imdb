import json
from Imdb.src.dto.dto import MovieDTO

class MovieService(object):
    def __init__(self, operations):
        self.operations =  operations

    def get_movies(self):
        try:
            # import pdb;pdb.set_trace()
            movies = self.operations.get_movies()
            movie_list =[]
            for each_movie in movies:
                genre = self.operations.get_genre(each_movie.movie_id)
                each_movie_obj= MovieDTO(each_movie.movie_id,
                                         each_movie.popularity,
                                         each_movie.director,
                                         each_movie.imdb_score,
                                         each_movie.movie_name,
                                         [each_genre.genre_name for each_genre in genre]
                                         )
                movie_list.append(each_movie_obj)
            return 200, json.dumps(movie_list, default=MovieDTO.dict_for_json, sort_keys=True)


            return 200, json.dumps('kp')
        except Exception as exception:
            print(exception)