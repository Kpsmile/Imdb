import os

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from Imdb.src.db.operations import UserOperations, MovieOperations
from Imdb.src.services.movie_service import MovieService
from Imdb.src.services.identity_service import IdentityService
from  Imdb.src.services.edit_movie_service import EditMovieService
from Imdb.src.services.delete_movie_service import DeleteMovieService
from Imdb.src.services.create_movie_service import CreateMovieService
from Imdb.src import imdb_application_maker

from Imdb.src.db import initialize_database_connectivity
from Imdb.config import config


class ImdbApplication(object):
    @staticmethod
    def init(dev_mode):
        port = config.get_application_port()

        """Initialize and connect to the database by getting the connection url params from the configuration file."""
        database_url = config.get_db_url()
        initialize_database_connectivity(database_url, pool_recycle=3600)

        """
        The below objects are initiated here and are injected to avoid dependencies into the classes, using
        constructor dependency injection
        """
        identity_service=IdentityService(UserOperations())
        create_service = CreateMovieService(MovieOperations())
        movie_service = MovieService(MovieOperations())
        edit_movie_service = EditMovieService(MovieOperations())
        delete_movies = DeleteMovieService(MovieOperations())

        imdb_application_maker.ApplicationMaker(dev_mode, identity_service,
                                                movie_service
                                                ,edit_movie_service
                                                ,delete_movies
                                                ,create_service
                                                ).make_app().listen(port)

        tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    """
    DEV_MODE is set to True in development mode for not to restart the server for every file changes.
    Should not be used in the production env, due to background processing consuming more memory.
    """
    ImdbApplication.init(os.getenv("DEV_MODE", False))
