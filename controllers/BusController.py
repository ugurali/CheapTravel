from flask import Blueprint, request
from services.BusService import BusService
from dto.Bus.TripRequest import TripRequest

import json

busController = Blueprint('busController', __name__, url_prefix="/busses")
busService = BusService()


@busController.route('/routes', methods=['POST'])
def routes():
    tripRequest = TripRequest.object_decoder(request.get_json())
    sourceId = busService.getStationId(tripRequest.source)
    destinationId = busService.getStationId(tripRequest.destination)

    response = {}
    response["direction1"] = busService.getRoute(sourceId,
                                                 destinationId,
                                                 tripRequest.departureDate,
                                                 tripRequest.adults,
                                                 tripRequest.children)

    if tripRequest.roundTrip:
        response["direction2"] = busService.getRoute(destinationId,
                                                     sourceId,
                                                     tripRequest.returnDate,
                                                     tripRequest.adults,
                                                     tripRequest.children)

    return json.dumps(response)
