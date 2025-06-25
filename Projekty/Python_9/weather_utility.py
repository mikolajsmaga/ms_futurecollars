from geopy.geocoders import Nominatim
import requests

def get_coordinate(city):
    # Pobiera i zwraca dane geograficzne (szerokość i długość) dla miasta
    geolocator = Nominatim(user_agent="weather_app")
    location = geolocator.geocode(city)
    if location:
        return location.latitude, location.longitude
    return None, None

def weather_api_url(latitude, longitude, date):
    # Buduje i zwraca URL do zapytania API Open-Meteo
    return (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={latitude}&longitude={longitude}&"
        f"hourly=rain&daily=rain_sum&timezone=Europe%2FLondon&"
        f"start_date={date}&end_date={date}"
    )

def ask_weather_data(url):
    # Wysyła zapytanie HTTP GET do podanego URL i zwraca dane JSON
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return {}
    except Exception:
        return {}

def analyze_rain_data(data):
    # Analizuje dane pogodowe i zwraca status opadów
    try:
        rain_sum = data.get("daily", {}).get("rain_sum", [])[0]
        if rain_sum > 0:
            return "Będzie padać"
        elif rain_sum == 0:
            return "Nie będzie padać"
        else:
            return "Nie wiem"
    except (IndexError, TypeError):
        return "Nie wiem"

def check_rain_status(city, date):
    # Łączy wszystkie kroki i zwraca ostateczną informację o deszczu dla miasta i daty
    latitude, longitude = get_coordinate(city)
    if latitude is None or longitude is None:
        return "Nie wiem (nie znaleziono miasta)"

    url = weather_api_url(latitude, longitude, date)
    data = ask_weather_data(url)
    return analyze_rain_data(data)

def get_rain_sum(city, date):
    # Ustalamy współrzędne miasta
    geolocator = Nominatim(user_agent="twoja_aplikacja")
    location = geolocator.geocode(city)

    if not location:
        return "Nie wiem (miasto nie znalezione)"

    latitude = location.latitude
    longitude = location.longitude

    # Budujemy URL do API
    url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={latitude}&longitude={longitude}&"
        f"hourly=rain&daily=rain_sum&timezone=Europe%2FLondon&"
        f"start_date={date}&end_date={date}"
    )

    # Wysyłamy zapytanie
    response = requests.get(url)

    if response.status_code != 200:
        return "Nie wiem (błąd API)"

    data = response.json()

    try:
        rain_sum = data.get("daily", {}).get("rain_sum", [])[0]
        # Interpretacja zgodnie z zadaniem
        if rain_sum > 0:
            return "Będzie padać"
        elif rain_sum == 0:
            return "Nie będzie padać"
        else:
            return "Nie wiem"
    except (IndexError, TypeError):
        return "Nie wiem"