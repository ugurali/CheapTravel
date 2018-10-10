from flask import Blueprint

carController = Blueprint('carController', __name__, url_prefix="/cars")


@carController.route('/routes', methods=['GET'])
def routes():
    return "Available cars"