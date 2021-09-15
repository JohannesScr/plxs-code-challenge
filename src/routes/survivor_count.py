from flask import Blueprint
from src.includes.utils import Response

survivor_count_ = Blueprint('survivor_count', __name__)


@survivor_count_.route('/survivorCount', methods=['POST'])
def post_survivor_count():
    """
    Endpoint is to return the survivor count for a given field grouped by
    bins. That is creating a histogram based on a field with specified
    number of bins.
    """
    return Response(message='survivors counted successfully',
                    data={}).create()
