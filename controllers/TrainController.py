from flask import Blueprint
from services.TrainService import TrainService

trainController = Blueprint('trainController', __name__, url_prefix="/trains")
trainService = TrainService()

@trainController.route('/routes', methods=['GET'])
def routes():
    return trainService.getRoute()
