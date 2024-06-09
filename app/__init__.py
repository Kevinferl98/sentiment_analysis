from flask import Flask
from .routes import bp
from .swagger import get_swaggerui

def create_app():
    app = Flask(__name__)
    app.register_blueprint(bp)
    app.register_blueprint(get_swaggerui())
    return app