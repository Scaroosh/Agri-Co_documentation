from flask import Blueprint

api_meteo_blueprint = Blueprint("api_meteo", __name__)


@api_meteo_blueprint.route("/api/meteo", methods=["GET"])
def api_meteo():
    # Import the required controllers or use cases
    from ..useCases.api_meteo_usecases import get_meteo_data

    # Call the controller methods or use case functions
    humidity, probability, rr10, rr1 = get_meteo_data("75056")

    return str(humidity) + " | " + str(probability), 200
