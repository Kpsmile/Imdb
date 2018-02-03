from Imdb.src.db.model import User,Role, Movie,Genre, MovieGenreMap


class CRUDBase(object):
    def __init__(self):
        pass

    def save(self, db_session, model_object):
        db_session.add(model_object)
        db_session.flush()
        return model_object

    def delete(self, db_session, model_object):
        db_session.delete(model_object)
        return model_object

class UserCRUD(CRUDBase):
    def get_user_role(self,db_session, user_name):

        user_role= db_session.query(User.role_id,Role.role_type).join(Role, Role.role_id == User.role_id).\
            filter(User.user_name==user_name).one()
        return user_role


class MovieCRUD(CRUDBase):

    def get_movies(self,db_session):
        movies = db_session.query(Movie).all()
        return  movies

    def get_genre(self,db_session,movie_id):
        genre = db_session.query(Genre.genre_name).join(MovieGenreMap,MovieGenreMap.genre_id == Genre.genre_id)\
            .filter(MovieGenreMap.movie_id == movie_id).all()
        return  genre

    def edit_movies(self,session, movie_id, popularity, director, imdb_score, movie_name):
        session.query(Movie).filter(Movie.movie_id == movie_id).\
            update({"popularity": popularity,
                    "director": director,
                    "imdb_score": imdb_score,
                    "movie_name": movie_name
                    })
        session.commit()
        movie = session.query(Movie.movie_id,
                              Movie.popularity,
                              Movie.director,
                              Movie.imdb_score,
                              Movie.movie_name). \
            filter(Movie.movie_name == movie_name).one()
        return movie

    def delete_movie(self, session,movie_id):
         return session.delete(session.query(Movie).filter_by(movie_id=movie_id).first())

    def save_movie(self, session, movie_data_model):
        self.save(session, movie_data_model)
        return movie_data_model.movie_id