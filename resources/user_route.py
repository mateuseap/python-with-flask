from flask import redirect, url_for
from flask_restful import Resource
import app

class UserRoute(Resource):
    def get(*args, **kwargs):
        user = app.User.query.get_or_404(kwargs['user_id'])
        return {"Username": user.name, "E-mail": user.email}