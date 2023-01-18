from flask_restful import Resource

class Index(Resource):
    def get(self):
        data = {"message": "Hello, world!"}
        return data