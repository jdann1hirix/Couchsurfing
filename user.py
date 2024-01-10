from datetime import datetime

def get_created_at_timestamp():
    return "2024-01-10 15:29:00"

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

USER = {
    "Fairy": {
        "uuid": "e340d0fa-3f91-4ca8-913d-e47c5d7d35c6",
        "name": "Tooth",
        "login": "Fairy",
        "created_at": get_created_at_timestamp(),
        "modified_at": get_created_at_timestamp(),
        "user_relationship": "3d402b31-e1f6-4b89-979e-4de0537f31c6",

    },
    "Ruprecht": {
        "uuid": "3d402b31-e1f6-4b89-979e-4de0537f31c6",
        "name": "Knecht",
        "login": "Ruprecht",
        "created_at": get_created_at_timestamp(),
        "modified_at": get_created_at_timestamp(),
        "user_relationship": "2bd31a35-c282-4c33-859e-cb89cb567498",
    },
    "Bunny": {
        "uuid": "2bd31a35-c282-4c33-859e-cb89cb567498",
        "name": "Easter",
        "login": "Bunny",
        "created_at": get_created_at_timestamp(),
        "modified_at": get_created_at_timestamp(),
        "user_relationship": "null",
    }
}

def read_all():
    return list(USER.values())