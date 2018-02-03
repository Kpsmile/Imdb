import tornado.web
from tornado import escape
from Imdb.src.handlers.imdb_request_handler import ImdbRequestHandler
import json


class EditMovieHandler(ImdbRequestHandler):
    """
    Class responsible for handling the edit movies API  call.
    Gets the edit movies details for the device in json format.
    """

    def initialize(self, edit_movie_service, identity_service):
        super(EditMovieHandler, self).initialize(identity_service)
        self.edit_movie_service = edit_movie_service
        self.identity_service = identity_service

    @tornado.web.asynchronous
    def put(self):
        """
        API : http://<ip>:<port>/1.0/edit/movies
        The put http request handler for the API call. The API updates the edit movies.
        :return: the json response containing message.
        """
        try:
            request_body = self.request.body
            status_code, message = self._call_service(request_body)
            self.set_status(status_code)
            self.write(message)
        except Exception as exception:
            self.write('Error while updating movie')
            self.set_status(404)
        finally:
            self.finish()

    def _call_service(self, request_body):
        """
        Using escape methods for Json to convert request body to native string type and
        passing it to edit movie service .
        :param request_body: Request body.
        :return: status_code and response message from the edit_movie Service.
        """
        request_body_decode = json.loads(str(escape.native_str(request_body)))
        status_code, message = self.edit_movie_service.edit_movie(
            request_body_decode['movie_id'],
            request_body_decode['popularity'],
            request_body_decode['director'],
            request_body_decode['imdb_score'],
            request_body_decode['movie_name'])
        return status_code, message