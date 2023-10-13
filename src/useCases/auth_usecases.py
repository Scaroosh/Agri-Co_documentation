global db


def does_email_exist(email):
    res = db.find_one({"email": email})
    return res is not None


def does_email_and_password_exist(email, password):
    res = db.find_one({"email": email, "password": password})
    return res is not None


def get_user_id(email, password):
    res = db.find_one({"email": email, "password": password})
    return str(res["_id"])
