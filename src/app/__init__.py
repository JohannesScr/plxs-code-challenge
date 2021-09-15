import logging
from dotenv import load_dotenv
from flask import Flask, jsonify
from src.includes.extends import cors
from src.app.config import get_config

logging.basicConfig(level=logging.DEBUG)


def create_server(env='.env'):
    """
    Creates an application instance of the server.
    """

    app = Flask(__name__)
    app.config.from_object(get_config(env))

    cors.init_app(app)

    @app.route('/', methods=['GET'])
    def home():
        return jsonify({'message': 'home'})

    return app
