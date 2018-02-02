import os

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

import Imdb
from Imdb.src.handlers import movie_handler, edit_movie_handler, delete_movie_handler, create_movie_handler


class ApplicationMaker(object):
    def __init__(self
                 , dev_mode=False
                 , identity_service=None
                 , movie_service=None
                 , edit_movie_service=None
                 , delete_movie_service=None
                 , create_movie_service=None
                 ):
        self.dev_mode = dev_mode
        self.identity_service = identity_service
        self.movie_service = movie_service
        self.edit_movie_service = edit_movie_service
        self.delete_movie_service = delete_movie_service
        self.create_movie_service = create_movie_service

    def make_app(self):
        settings = {"static_path": os.path.join(Imdb.ROOT_DIR, 'static'), "static_url_prefix": "/static/"}
        application = tornado.web.Application(self._get_api_handlers_mapping(), debug=self.dev_mode, **settings)
        return application

    def _get_api_handlers_mapping(self):
        apis = ['movies'
                , 'edit_movie'
                , 'delete_movie'
                , 'create_movie'
                ]
        return [self._get_api_mapping(api) for api in apis]

    def _get_api_mapping(self, api):
        if api == 'create_movie':
            return (r"/1.0/movie/create", create_movie_handler.CreateMovieHandler,
                    dict(create_movie_service=self.create_movie_service, identity_service=self.identity_service))
        if api == 'edit_movie':
            return (r"/1.0/movie/edit", edit_movie_handler.EditMovieHandler,
                    dict(edit_movie_service=self.edit_movie_service, identity_service=self.identity_service))
        if api == 'delete_movie':
            return (r"/1.0/movie/delete", delete_movie_handler.DeleteMovieHandler,
                    dict(delete_movie_service=self.delete_movie_service, identity_service=self.identity_service))
        if api == 'movies':
            return (r"/1.0/movies", movie_handler.MovieHandler,
                    dict(movie_service=self.movie_service, identity_service=self.identity_service))
