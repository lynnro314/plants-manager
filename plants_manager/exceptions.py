import json
# from plants_manager.main import app
from werkzeug.exceptions import HTTPException
from plants_manager.model import OPTIONAL_PARAMS, MANDATORY_PARAMS

class PlantsBaseException(HTTPException):
    pass


class PlantNotFoundException(PlantsBaseException):
    code = 404

    def __init__(self, name):
        description =  "Plant %s doesn't exist." % name
        super(PlantsBaseException, self).__init__(description)


class WrongPlantParameters(PlantsBaseException):
    code = 400

    def __init__(self):
        params_list = ', '.join(OPTIONAL_PARAMS)
        description =  'Request has one or more wrong parameters. ' \
               'The relevant parameters are: %s' % params_list
        super(PlantsBaseException, self).__init__(description)


class MissingKeyParameters(PlantsBaseException):
    code = 400

    def __init__(self):
        params_list = ', '.join(MANDATORY_PARAMS)
        description =  'Missing mandatory parameter. ' \
           'All records should have the parameters: %s' % params_list
        super(PlantsBaseException, self).__init__(description)


class AlreadyExistsException(PlantsBaseException):
    code = 409

    def __init__(self, name):
        description =  'Plant %s already exists.' %name
        super(PlantsBaseException, self).__init__(description)


def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    # start with the correct headers and status code from the error
    response = e.get_response()
    # replace the body with JSON
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response