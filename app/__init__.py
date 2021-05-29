from flask import Flask
from app.controllers import api_bp
from app.templates import page_bp


def create_app(*config):
    app = Flask(__name__, template_folder='templates')

    app.register_blueprint(page_bp)
    app.register_blueprint(api_bp)

    return app
