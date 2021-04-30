from pymongo import errors as mongo_errors
from plants_manager import exceptions
from plants_manager import helpers
from plants_manager.model import PLANTS


def create_plant(new_plant):
    helpers.check_mandatory_parameters(new_plant)
    helpers.check_wrong_parameters(new_plant)
    name = new_plant['name']
    try:
        plant_id = PLANTS.insert_one(new_plant)
    except mongo_errors.DuplicateKeyError:
        raise exceptions.AlreadyExistsException(name)
    plant = new_plant.update({"id": str(plant_id)})
    return plant


def list_plants():
    all_plants = PLANTS.find()
    return [helpers.parse_result(r) for r in all_plants]


def get_plant(name):
    plant = PLANTS.find_one({'name': name})
    if plant is None:
        raise exceptions.PlantNotFoundException(name)
    return helpers.parse_result(plant)


def update_plant(name, plant):
    helpers.check_wrong_parameters(plant)
    try:
        plant = PLANTS.find_one_and_update({'name': name}, plant)
    except mongo_errors.DuplicateKeyError:
        raise exceptions.AlreadyExistsException(name)
    except ValueError:
        # TODO:: Handle exception
        pass
    if plant is None:
        raise exceptions.PlantNotFoundException(name)
    return helpers.parse_result(plant)


def delete_plant(name):
    deleted_plant = PLANTS.find_one_and_delete({'name': name})
    if deleted_plant is None:
        raise exceptions.PlantNotFoundException(name)
    return helpers.parse_result(deleted_plant)
