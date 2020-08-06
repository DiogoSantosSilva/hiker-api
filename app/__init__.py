# app/__init__.py

from flask_restplus import Api
from flask import Blueprint

from .main.controller.user_controller import api as user_api
from .main.controller.auth_controller import api as auth_api

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='FLASK RESTPLUS API',
          version='1.0',
          description='a boilerplate for flask restplus web service'
          )

api.add_namespace(user_api, path='/user')
api.add_namespace(auth_api)