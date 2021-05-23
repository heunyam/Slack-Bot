from flask import Flask
from app.views import bp


def create_app(*config):
    app = Flask(__name__)
    app.register_blueprint(bp)

    return app
