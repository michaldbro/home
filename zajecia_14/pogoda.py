import requests
from file_handler import FileHandler

def get_weather_api(day):
    url = f"https://api.open-meteo.com/v1/forecast?latitude=52.2337172&longitude=21.0714322&hourly=rain&daily=rain_sum&timezone=Europe%2FLondon&start_date={day}&end_date={day}"
    response = requests.get(url)
    return response.json()

def sum_opad(response_data):
    if not response_data:
        return {}
    opad = response_data.get("rain_sum", {})
    wynik = {
        #"rain": opad.get("rain_sum", "N/A")
        "rain": opad.get("rain_sum")
    }
    return wynik

file_handler = FileHandler(file_path="data.json")
day="2025-06-15"
print('Program sprawdzający czy będzie padać w Warszawie')
#day = input('Podaj dzień (w formacie YYYY-MM-DD): ')
response_data = get_weather_api(day)
#get_weather = get_weather_api(day)
#print(get_weather)
suma_opadow = sum_opad(response_data)
wartosc_opadow = [suma_opadow]
#print(suma_opadow)
value = suma_opadow['rain'][0]
value_float = float(value)
print(value)
print(value_float)

if value1 := file_handler.search_in_file(value_float):
    print("Dane są w pliku:")
    if value1 == 0.0:
        print('Nie będzie padać')
    elif value1 > 0.0:
        print('Będzie padać')
    else:
        print('Nie wiem')
else:
    if value == 0.0:
        print('Nie będzie padać')
    elif value > 0.0:
        print('Będzie padać')
    else:
        print('Nie wiem')
    value_1 = sum_opad(response_data)
    file_handler.write_file(value_1)


