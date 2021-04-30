import os
import pymongo

MANDATORY_PARAMS = {"name" ,"family", "type"}
OPTIONAL_PARAMS = {"weather", "details"}
SUPPORTED_PARAMS = MANDATORY_PARAMS.union(OPTIONAL_PARAMS)

DB_NAME = os.getenv('MONGODB_DATABASE')
COLLECTION_NAME = os.getenv('COLLECTION_NAME')

def mongo_uri():
    user = os.getenv('MONGODB_USERNAME')
    password = os.getenv('MONGODB_PASSWORD')
    hostname = os.getenv('MONGODB_HOSTNAME')
    if not all((user, password, hostname)):
        # TODO:: Fail?
        pass
    return 'mongodb://%s:%s@%s:27017/' % (user, password, hostname)


def init_db():
    # TODO:: check if we need to remove connect=False.
    client = pymongo.MongoClient(mongo_uri(), connect=False)
    db = client[DB_NAME]
    plants = db[COLLECTION_NAME]
    plants.create_index("name", unique=True)
    return plants


PLANTS = init_db()
