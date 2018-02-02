from contextlib import contextmanager

from Imdb.src.db import create_session
from Imdb .src.db.crud import CRUDBase, UserCRUD,MovieCRUD



@contextmanager
def transactional_session():
    """Provide a transactional scope around a series of operations."""
    session = create_session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


class OperationsBase(object):
    def __init__(self, crud=None):
        self.crud = crud if crud is not None else CRUDBase()

    def save(self, model):
        with transactional_session() as session:
            model = self.crud.save(session, model)
            session.expunge(model)
            return model

    def bulk_save(self, model_list):
        with transactional_session() as session:
            self.crud.bulk_save(session, model_list)

    def fetch(self, model):
        with transactional_session() as session:
            models = self.crud.fetch_all(session, model)
            session.expunge_all()
            return models

class UserRoleInfo(object):
    def __init__(self, role_id, role_type):
        self.role_id = role_id
        self.role_type = role_type

class UserOperations(OperationsBase):
    def __init__(self, user_crud=None):
        super(UserOperations, self).__init__()
        self.user_crud = user_crud if user_crud is not None else UserCRUD()

    def get_user_role(self, username):
        with transactional_session() as session:
            user=self.user_crud.get_user_role(session, username)
            user_role = UserRoleInfo(user.role_id, user.role_type)
        return user_role

class MovieInfo(object):
    def __init__(self, movie_id, popularity, director, imdb_score, movie_name):
        self.movie_id= movie_id
        self.popularity = popularity
        self.director = director
        self.imdb_score = imdb_score
        self.movie_name = movie_name

class GenreInfo(object):
    def __init__(self, genre_name):
        self.genre_name = genre_name


class MovieOperations(OperationsBase):
    def __init__(self, movie_crud=None):
        super(MovieOperations, self).__init__()
        self.movie_crud = movie_crud if movie_crud is not None else MovieCRUD()

    def get_movies(self):
        with transactional_session() as session:
            movie_list = self.movie_crud.get_movies(session)
            movies = [MovieInfo(each_movie.movie_id, each_movie.popularity, each_movie.director,
                                   each_movie.imdb_score, each_movie.movie_name) for each_movie in movie_list]
        return movies

    def get_genre(self, movie_id):
        with transactional_session() as session:
            genre_list = self.movie_crud.get_genre(session, movie_id)
            genres = [GenreInfo(each_genre.genre_name) for each_genre in genre_list]
        return genres

    def edit_movies(self, movie_id, popularity, director, imdb_score, movie_name):
        with transactional_session() as session:
            return self.movie_crud.edit_movies(session, movie_id,popularity, director, imdb_score, movie_name)

    def delete_movie(self, movie_id):
        with transactional_session() as session:
            return self.movie_crud.delete_movie(session, movie_id)

    def save_movie(self, movie_data_model):
        with transactional_session() as session:
            return self.movie_crud.save_movie(session, movie_data_model)