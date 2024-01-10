from datetime import datetime
import uuid

def get_created_at_timestamp():
    return "2024-01-10T15:29:00"

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%dT%H:%M:%S"))

USER = {
    "Fairy": {
        "uuid": "e340d0fa-3f91-4ca8-913d-e47c5d7d35c6",
        "login": "Fairy",
        "created_at": get_created_at_timestamp(),
        "modified_at": get_created_at_timestamp(),
        "user_relationship_id": "3d402b31-e1f6-4b89-979e-4de0537f31c6",

    },
    "Ruprecht": {
        "uuid": "3d402b31-e1f6-4b89-979e-4de0537f31c6",
        "login": "Ruprecht",
        "created_at": get_created_at_timestamp(),
        "modified_at": get_created_at_timestamp(),
        "user_relationship_id": "2bd31a35-c282-4c33-859e-cb89cb567498",
    },
    "Bunny": {
        "uuid": "2bd31a35-c282-4c33-859e-cb89cb567498",
        "login": "Bunny",
        "created_at": get_created_at_timestamp(),
        "modified_at": get_created_at_timestamp(),
        "user_relationship_id": "null",
    }
}

def read_all():
    return list(USER.values())

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
