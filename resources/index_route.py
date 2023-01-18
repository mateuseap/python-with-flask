from flask_restful import Resource
import app

class IndexRoute(Resource):
    def get(self):
        users = app.User.query.all() 
        return {"Username": users[1].name, "E-mail": users[1].email}