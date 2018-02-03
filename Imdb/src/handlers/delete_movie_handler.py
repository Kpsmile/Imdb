import tornado.web
from tornado import escape
from Imdb.src.handlers.imdb_request_handler import ImdbRequestHandler
import json


class DeleteMovieHandler(ImdbRequestHandler):
    """
    Class responsible for handling the delete movie API  call.
    """

    def initialize(self, delete_movie_service, identity_service):
        super(DeleteMovieHandler, self).initialize(identity_service)
        self.delete_movie_service = delete_movie_service
        self.identity_service = identity_service

    @tornado.web.asynchronous
    def delete(self):
        """
        API : http://<ip>:<port>/1.0/movie/delete
        The delete http request handler for the API call. The API delete the  movie.
        :return: the json response containing message.
        """
        try:
            request_body = self.request.body
            status_code, message = self._call_service(request_body)
            self.set_status(status_code)
            self.write(message)
        except Exception as exception:
            self.write('Error while deleteing movie')
            self.set_status(404)
        finally:
            self.finish()

    def _call_service(self, request_body):
        """
        Using escape methods for Json to convert request body to native string type and
        passing it to delete movie service .
        :param request_body: Request body.
        :return: status_code and response message from the delete_movie Service.
        """
        request_body_decode = json.loads(str(escape.native_str(request_body)))
        status_code, message = self.delete_movie_service.delete_movie(
            request_body_decode['movie_id'])
        return status_code, message