from datetime import datetime
from flask import abort, make_response
import uuid

def get_created_at_timestamp():
    return "2024-01-10T15:29:00"

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%dT%H:%M:%S"))

USER = {
    "98a2bb91-7df2-4b3d-a833-7d1e4c572739": {
        "uuid": "98a2bb91-7df2-4b3d-a833-7d1e4c572739",
        "login": "User 0 - Not related at all",
        "created_at": get_created_at_timestamp(),
        "modified_at": get_created_at_timestamp(),
        "user_relationship_id": "null",

    },
    "e340d0fa-3f91-4ca8-913d-e47c5d7d35c6": {
        "uuid": "e340d0fa-3f91-4ca8-913d-e47c5d7d35c6",
        "login": "User 1 - Relation User 2",
        "created_at": get_created_at_timestamp(),
        "modified_at": get_created_at_timestamp(),
        "user_relationship_id": "3d402b31-e1f6-4b89-979e-4de0537f31c6",

    },
    "3d402b31-e1f6-4b89-979e-4de0537f31c6": {
        "uuid": "3d402b31-e1f6-4b89-979e-4de0537f31c6",
        "login": "User 2 - Related user 3",
        "created_at": get_created_at_timestamp(),
        "modified_at": get_created_at_timestamp(),
        "user_relationship_id": "2bd31a35-c282-4c33-859e-cb89cb567498",
    },
    "2bd31a35-c282-4c33-859e-cb89cb567498": {
        "uuid": "2bd31a35-c282-4c33-859e-cb89cb567498",
        "login": "User 3 - Related to User 4",
        "created_at": get_created_at_timestamp(),
        "modified_at": get_created_at_timestamp(),
        "user_relationship_id": "8fab2601-d22d-448b-b9fe-0bc920622461",
    },
    "8fab2601-d22d-448b-b9fe-0bc920622461": {
        "uuid": "8fab2601-d22d-448b-b9fe-0bc920622461",
        "login": "User 4 - Related user 5",
        "created_at": get_created_at_timestamp(),
        "modified_at": get_created_at_timestamp(),
        "user_relationship_id": "2c0376c4-b65a-4e17-85b8-b338e38614db",
    }
    ,
    "2c0376c4-b65a-4e17-85b8-b338e38614db": {
        "uuid": "2c0376c4-b65a-4e17-85b8-b338e38614db",
        "login": "User 5 - Related user 2",
        "created_at": get_created_at_timestamp(),
        "modified_at": get_created_at_timestamp(),
        "user_relationship_id": "null",
    }
}

def read_all():
    return list(USER.values())

def read_one(uuid):
    if uuid in USER:
        return USER[uuid]
    else:
        abort(
            404, f"User with id {uuid} not found"
        )

def create(user):
    uuidnumber = str(uuid.uuid4())
    login = user.get("login")
    user_relationship_id = user.get("user_relationship_id", "")

    USER[uuidnumber] = {
            "uuid": uuidnumber,
            "login": login,
            "user_relationship_id": user_relationship_id,
            "created_at": get_timestamp(),
            "modified_at": get_timestamp(),
    }

    return USER[uuidnumber], 201

def update(uuid, user):
    if uuid in USER:
        USER[uuid]["login"] = user.get("login")
        USER[uuid]["user_relationship_id"] = user.get("user_relationship_id")
        USER[uuid]["modified_at"] = get_timestamp()
        return USER[uuid]
    else:
        abort(
            404,
            f"User with id {uuid} not found"
        )

def delete(uuid):
    if uuid in USER:
        del USER[uuid]
        return make_response(
            f"User {uuid} successfully deleted", 200
        )
    else:
        abort(
            404,
            f"User with id {uuid} not found"
        )

def relationship_level(uuid, uuid_to_search):
    if uuid not in USER:
        abort(
                404,
                f"User with id {uuid} not found"
            )
    if uuid_to_search not in USER:
        abort(
                404,
                f"User with id {uuid_to_search} not found"
            )
        
    if USER[uuid]["user_relationship_id"] == "null":
        abort(
                404,
                f"User with id {uuid} has no relationships "
            )
        
    relationship_level = map_relationship(uuid, uuid_to_search)
    return_message = ""
    if (relationship_level == 0):
        return_message = f"User with id {uuid} has no relationship with {uuid_to_search}"
    else:
        return_message = f"User with id {uuid} has a {relationship_level} degree relationship with {uuid_to_search}"

    return make_response(return_message, 200)
    

def map_relationship(uuid, uuid_to_search, relationship_level = 0, found_relation = False): 
    relationship_current_user = USER[uuid]

    while not found_relation:
        relationship_level = relationship_level + 1

        if (relationship_current_user["user_relationship_id"] == "null"):
            break
        else:
            if (relationship_current_user["user_relationship_id"] == uuid_to_search): 
                found_relation = True
            else:
                relationship_current_user = USER[relationship_current_user["user_relationship_id"]]

    
    if (found_relation):
        return relationship_level
    else:
        return 0
        
