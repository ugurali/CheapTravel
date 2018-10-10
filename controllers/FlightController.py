from flask import Blueprint, request
from services.FlightService import FlightService
from dto.Flight.TripRequest import TripRequest

flightController = Blueprint('flightController', __name__, url_prefix="/flights")


@flightController.route('/routes', methods=['POST'])
def routes():
    flightService = FlightService()
    tripRequest = TripRequest.object_decoder(request.get_json())

    #sessionId = flightService.createSession('DE', 'EUR', 'de-DE', 'MUC-sky', 'IST-sky', '2018-11-01', '2018-11-02', 'economy', '1', '0', '0')
    #sessionId = '2b77a0e2d9c448bf964f582079a31e06_rrsqbjcb_cd8283034710069eed7028483edbcb3e'
    sessionId = flightService.createSession(tripRequest.country,
                                            tripRequest.currency,
                                            tripRequest.locale,
                                            tripRequest.origin,
                                            tripRequest.destination,
                                            tripRequest.outboundDate,
                                            tripRequest.inboundDate,
                                            tripRequest.cabinClass,
                                            tripRequest.adults,
                                            tripRequest.children,
                                            tripRequest.infants)

    return flightService.getRoutesFromSession(sessionId)