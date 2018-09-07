PROFILE_KEYS = ("fname", "lname", "age")


def profile_data_validator(data):
    keys = list(data.keys())
    for k in keys:
        if not k in PROFILE_KEYS:
            return False
    if "fname" in data:
        if not isinstance(data["fname"], str):
            return False
    if "lname" in data:
        if not isinstance(data["lname"], str):
            return False
    if "age" in data:
        if not isinstance(data["age"], str):
            return False
    return True