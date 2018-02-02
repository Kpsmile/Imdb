import tornado.web
from tornado import escape
from Imdb.src.handlers.imdb_request_handler import ImdbRequestHandler
from Imdb.src.db.model import Movie
import json


class CreateMovieHandler(ImdbRequestHandler):
    """
    Class responsible for handling the create movie API  call.
    """

    def initialize(self, create_movie_service, identity_service):
        super(CreateMovieHandler, self).initialize(identity_service)
        self.create_movie_service = create_movie_service
        self.identity_service = identity_service


    @tornado.web.asynchronous
    def post(self):
        """
        API : http://<ip>:<port>/1.0/movie/create
        The put http request handler for the API call. The API create the  movie.
        :return: the json response containing message.
        """
        try:
            request_body = self.request.body
            movie_data_model = self._call_service(request_body)
            status_code, message = self.create_movie_service.create_movie(movie_data_model)
            self.set_status(status_code)
            self.write(message)
        except Exception as exception:
            self.write('Error creating movie')
            self.set_status(404)
        finally:
            self.finish()

    def _call_service(self, request_body):
        """
        Using escape methods for Json to convert request body to native string type and
        passing it to create movie service .
        :param request_body: Request body.
        :return: movie_data_model
        """
        movie_data = json.loads(str(escape.native_str(request_body)))
        movie_data_model = Movie(movie_id=None,
                                 popularity=movie_data['popularity'],
                                 director=movie_data['director'],
                                 imdb_score=movie_data['imdb_score'],
                                 movie_name=movie_data['movie_name'])
        return movie_data_model

