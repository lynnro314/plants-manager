from plants_manager import exceptions
from plants_manager import helpers
from plants_manager.model import PLANTS


def create_plant(new_plant):
    helpers.check_mandatory_parameters(new_plant)
    helpers.check_wrong_parameters(new_plant)
    name = new_plant['name']
    if name in PLANTS:
        raise exceptions.AlreadyExistsException(name)
    PLANTS[name] = new_plant
    return new_plant


def list_plants():
    return PLANTS


def get_plant(name):
    helpers.check_plant_exists(name)
    return PLANTS.get(name)


def update_plant(name, plant):
    helpers.check_plant_exists(name)
    if 'name' in plant.keys():
        helpers.check_same_name(name, plant)
    helpers.check_wrong_parameters(plant)
    PLANTS[name].update(plant)
    return plant


def delete_plant(name):
    helpers.check_plant_exists(name)
    deleted_plant = PLANTS.pop(name)
    return deleted_plant