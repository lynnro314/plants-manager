from plants_manager.model import MANDATORY_PARAMS, TABLE_PARAMS, PLANTS
from plants_manager import exceptions

def check_wrong_parameters(plant):
    if any(key not in TABLE_PARAMS for key in plant.keys()):
        raise exceptions.WrongPlantParameters()


def check_mandatory_parameters(plant):
    if not all(key in plant.keys() for key in MANDATORY_PARAMS):
        raise exceptions.MissingKeyParameters()


def check_plant_exists(name):
    if PLANTS.get(name) is None:
        raise exceptions.PlantNotFoundException(name)


def check_same_name(name, plant):
    if name != plant['name']:
        raise exceptions.WrongNameException(name)
