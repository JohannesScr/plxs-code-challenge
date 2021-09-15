from flask import Blueprint
from src.includes.utils import Response

home_ = Blueprint('home', __name__)


@home_.route('/', methods=['GET'])
def home():
    """
    Default landing for the server.
    """
    return Response(message='Welcome to this server').create()
