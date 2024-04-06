# Initializes the Flask application and sets up configurations and blueprints.
from flask import Flask
from .views import main_blueprint


def create_app():
    app = Flask(__name__)
    app.register_blueprint(main_blueprint)  # Register blueprint from app/views.py
    return app
