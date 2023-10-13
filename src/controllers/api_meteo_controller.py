import requests
from dotenv import dotenv_values

# Load environment variables
env_vars = dotenv_values(".env")
token = env_vars.get("API_CONCEPT_TOKEN", "")


def get_humidity(code):
    url = f"https://api.meteo-concept.com/api/forecast/nextHours?token={token}&insee={code}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        humidity = data["forecast"][0]["rh2m"]
        return humidity
    except requests.exceptions.RequestException as e:
        print(e)
        return "[GETHUMIDITY] Request failed"


def check_rain(code):
    url = f"https://api.meteo-concept.com/api/forecast/daily?token={token}&insee={code}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        forecast = data["forecast"][0]
        probability = forecast["probarain"]
        rr10 = forecast["rr10"]
        rr1 = forecast["rr1"]
        return probability, rr10, rr1
    except requests.exceptions.RequestException as e:
        print(e)
        return 0, 0, 0  # Return default values or handle the error appropriately
