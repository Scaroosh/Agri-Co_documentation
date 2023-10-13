from flask import Blueprint, request
from ..controllers.auth_controller import register, login, delete

auth_routes_blueprint = Blueprint("user_routes", __name__)


@auth_routes_blueprint.route("/register", methods=["POST"])
def register_route():
    data = request.get_json()
    return register(data)


@auth_routes_blueprint.route("/login", methods=["POST"])
def login_route():
    data = request.get_json()
    return login(data)


@auth_routes_blueprint.route("/delete", methods=["DELETE"])
def delete_route():
    data = request.get_json()
    return delete(data)
