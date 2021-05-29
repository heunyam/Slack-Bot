from flask_restful import Api
from flask import Blueprint

from app.controllers.slack_event import HelloAPI

api_bp = Blueprint('api', __name__)

api = Api(api_bp)
api.add_resource(HelloAPI, '/')
