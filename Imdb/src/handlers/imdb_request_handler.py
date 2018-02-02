import tornado.web

class ImdbRequestHandler(tornado.web.RequestHandler):

    def initialize(self, idenity_service):
        self.idenity_service = idenity_service

    def prepare(self):
        try:
            if len(self.request.headers) > 0:
                token = str(self.request.headers['Authorization'])
                user_role = self.idenity_service.get_user_role(token)
                if user_role != 'admin':
                    self.set_status(401)
                    self.write('Unauthorized: The request requires user authentication.')
                    self.flush()
                    self.finish()
            else:
                self.set_status(403)
                self.write('Authorization failed')
                self.flush()
                self.finish()
        except KeyError as e:
            self.set_status(403)
            self.write('Authorization failed')
            self.flush()
            self.finish()