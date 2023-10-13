from ..useCases.auth_usecases import (
    does_email_exist,
    does_email_and_password_exist,
    get_user_id,
)
from flask import jsonify
from bson import ObjectId

global db


def register(data):
    if not does_email_exist(data["email"]):
        db.insert_one(
            {
                "email": data["email"],
                "password": data["password"],
            }
        )
        return jsonify({"message": "Register successful!"}), 201

    return jsonify({"message": "An account with that email already exists!"}), 400


def login(data):
    if does_email_and_password_exist(data["email"], data["password"]):
        user_id = get_user_id(data["email"], data["password"])
        return jsonify({"message": "Successfully Logged In", "user_id": user_id}), 200

    return jsonify({"message": "Incorrect login or password"}), 400


def update(data):
    res = db.find_one_and_update({"_id": ObjectId(data["user_id"])}, data)
    if res is not None:
        return jsonify({"message": "Update success"}), 200
    return jsonify({"message": "Can't update this account"}), 400


def delete(data):
    res = db.find_one_and_delete({"_id": ObjectId(data["user_id"])})
    if res is not None:
        return jsonify({"message": "Delete success"}), 200
    return jsonify({"message": "Can't delete this account"}), 400


def get_info(data):
    res = db.find_one({"_id": ObjectId(data["user_id"])})
    if res is not None:
        return jsonify(res), 200
    return jsonify({"message": "Couldn't retrieve info"}), 400
