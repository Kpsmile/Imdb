import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from Imdb.src.handlers.imdb_request_handler import ImdbRequestHandler

class MovieHandler(ImdbRequestHandler):
    """
    Class responsible for handling the Alerts API  call.
    Gets the Alerts details for the device in json format.
    """

    def initialize(self, movie_service, identity_service):
        super(MovieHandler, self).initialize(identity_service)
        self.movie_service = movie_service
        self.identity_service = identity_service

    @tornado.web.asynchronous
    def get(self):
        """
        API :   http://<ip>:<port>/movies/
        The get http request handler for the Movies API  call '/'.
        The response of the API is  movie details in json format .
        """
        try:
            # import pdb;pdb.set_trace()
            http_status, alert_data = self.movie_service.get_movies()
            self.set_status(http_status)
            self.write(alert_data)
        except:
            self.write('The request processing has failed because of an unknown error, exception or failure')
            self.set_status(200)
        finally:
            self.finish()

