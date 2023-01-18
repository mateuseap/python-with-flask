import traceback
from werkzeug.wrappers import Request, Response

class Auth(object):
    def __init__(self, app):
        self.app = app
        self.api_key = 'e6db8bdb-0291-4458-965e-7e6a9c5ab1b6'

    def __call__(self, environ, start_response):
        try:
            request = Request(environ)
            api_key = request.headers['API_KEY']

            if self.api_key == api_key:
                return self.app(environ, start_response)
            else:
                response = Response('Authorization Failed', mimetype='text/plain', status=401)
                return response(environ, start_response)
        except:
            response = Response('Internal Server Error', mimetype='text/plain', status=500)
            return response(environ, start_response)