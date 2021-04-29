import json
# from plants_manager.main import app
from werkzeug.exceptions import HTTPException
from plants_manager.model import TABLE_PARAMS, MANDATORY_PARAMS

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
        description =  'Request has one or more wrong parameters. ' \
               'The relevant parameters are: ' + ', '.join(TABLE_PARAMS)
        super(PlantsBaseException, self).__init__(description)


class MissingKeyParameters(PlantsBaseException):
    code = 400

    def __init__(self):
        description =  'Missing mandatory parameter. ' \
           'All records should have the parameters: ' + ', '.join(MANDATORY_PARAMS)
        super(PlantsBaseException, self).__init__(description)


class WrongNameException(PlantsBaseException):
    code = 400

    def __init__(self, name):
        description =  'Can not rename an existing plant. The name should be %s.' %name
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