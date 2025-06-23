import requests
from file_handler import FileHandler
from geopy.geocoders import Nominatim
from datetime import datetime, timedelta

def get_weather_api(day, city):
    geolocator = Nominatim(user_agent="michal_dbr_app")
    location = geolocator.geocode(city)
    latitude = location.latitude
    longitude = location.longitude
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=rain&daily=rain_sum&timezone=Europe%2FLondon&start_date={day}&end_date={day}"
    response = requests.get(url=url)
    data = response.json()
    if not data:
        return {}
    #opad = data.get("daily", {}).get("rain_sum", [])[0]
    wynik = {
        "city": city,
        "rain": data.get("daily", {}).get("rain_sum", [])[0]
    }
    return wynik

file_handler = FileHandler(file_path="data.json")

(print('Program sprawdzający czy będzie padać'))
city = input('Podaj Nazwę miasta dla którego szukać danych (np. Warszawa): ')
while True:
    day_imput = input("Podaj datę - wymagany format: YYYY-MM-DD (np. 2025-05-20): ")
    if not day_imput.strip():  # jeśli użytkownik nic nie wpisał
        day = datetime.now().date() + timedelta(days=1)
        print(f"Nie podano daty. Ustawiono datę jutrzejszą: {day}")
        break
    else:
        try:
            day = datetime.strptime(day_imput, "%Y-%m-%d").date()
            print(f"Ustawiono datę: {day}")
            break
        except ValueError:
            print("Uwaga Błąd: Niepoprawny format daty. Użyj formatu YYYY-MM-DD.")

value = get_weather_api(day, city).get("rain")
value_2 = get_weather_api(day, city).get("city")
rain_in_file = file_handler.search_in_file(value, value_2)

result = file_handler.search_in_file(value, value_2)
if result and value_2 == result.get("city") and value == result.get("rain"):
    print(f"Suma opadów wynosi: {value} - Dane są w pliku:")
    if value == 0:
        print('Nie będzie padać')
    elif value > 0:
        print('Będzie padać')
    else:
        print('Nie wiem')
else:
    print(f"Suma opadów wynosi: {value} - Nie znaleziono danych w pliku dla tej wartości")
    file_handler.write_file(get_weather_api(day, city))
    print('Dane pobrane z API')
    if value == 0:
        print('Nie będzie padać')
    elif value > 0:
        print('Będzie padać')
    else:
        print('Nie wiem')
    print("Dane zapisane do pliku")