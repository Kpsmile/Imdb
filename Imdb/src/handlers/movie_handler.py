import tornado.web
class MovieHandler(tornado.web.RequestHandler):
    """
    Class responsible for handling the get movies API  call.
    Gets the movies details  in json format.
    """
    def __init__(self, application, request, **kwargs):
        super(MovieHandler, self).__init__(application, request, **kwargs)

    def initialize(self, movie_service):
        self.movie_service = movie_service

    @tornado.web.asynchronous
    def get(self):
        """
        API :   http://<ip>:<port>/movies/
        The get http request handler for the Movies API  call '/'.
        The response of the API is  movie details in json format .
        """
        try:
            http_status, alert_data = self.movie_service.get_movies()
            self.set_status(http_status)
            self.write(alert_data)
        except:
            self.write('The request processing has failed because of an unknown error, exception or failure')
            self.set_status(200)
        finally:
            self.finish()

