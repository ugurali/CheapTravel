from flask import Flask
from controllers.BusController import busController
from controllers.CarController import carController
from controllers.FlightController import flightController
from controllers.TrainController import trainController

app = Flask(__name__)

app.register_blueprint(busController)
app.register_blueprint(carController)
app.register_blueprint(flightController)
app.register_blueprint(trainController)

@app.route('/')
def hello_world():
    return 'Welcome to Cheap Travel!'


if __name__ == '__main__':
    app.run()
