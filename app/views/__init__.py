from flask_restful import Api
from flask import Blueprint

from app.views.slack_event import HelloAPI


bp = Blueprint('api', __name__)
api = Api(bp)

api.add_resource(HelloAPI, '/')
