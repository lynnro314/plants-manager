from plants_manager.model import MANDATORY_PARAMS, SUPPORTED_PARAMS
from plants_manager import exceptions

def check_wrong_parameters(plant):
    if not plant or any(key not in SUPPORTED_PARAMS for key in plant.keys()):
        raise exceptions.WrongPlantParameters()


def check_mandatory_parameters(plant):
    if not plant or not all(key in plant.keys() for key in MANDATORY_PARAMS):
        raise exceptions.MissingKeyParameters()


def parse_result(data):
    # Convert _id bson object to str
    data['id'] = str(data.pop('_id'))
    return data
