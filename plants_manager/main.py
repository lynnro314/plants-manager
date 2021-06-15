import logging
from flask import Flask, request, jsonify
from plants_manager import controller
from plants_manager.exceptions import PlantsBaseException, handle_exception

app = Flask(__name__)
app.register_error_handler(PlantsBaseException, handle_exception)
logging.basicConfig(level=logging.INFO)


@app.route('/v1/plants', methods=['POST'])
def create_plant():
    data = request.json
    app.logger.info(data)
    new_plant = controller.create_plant(data)
    return new_plant, 201

@app.route('/v1/plants', methods=['GET'])
def list_plants():
    plants = controller.list_plants()
    response = jsonify(plants)
    return response, 200

@app.route('/v1/plants/<name>', methods=['GET'])
def get_plant(name):
    plant = controller.get_plant(name)
    return plant, 200

@app.route('/v1/plants/<name>', methods=['PATCH'])
def update_plant(name):
    data = request.json
    app.logger.info(data)
    plant = controller.update_plant(name, data)
    return plant, 201

@app.route('/v1/plants/<name>', methods=['DELETE'])
def delete_plant(name):
    deleted_plant = controller.delete_plant(name)
    return deleted_plant, 201
