from ..controllers.api_meteo_controller import get_humidity, check_rain


def get_meteo_data(code):
    humidity = get_humidity(code)
    probability, rr10, rr1 = check_rain(code)
    return humidity, probability, rr10, rr1
