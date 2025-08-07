import requests

def get_place_coordinates(location_name, api_key):
    # modul do szukania lon lat po nazie miasta
    geocode_url = f"https://maps.googleapis.com/maps/api/geocode/json?address={location_name}&key={api_key}"
    response = requests.get(geocode_url).json()
    if response['status'] == 'OK':
        latlng = response['results'][0]['geometry']['location']
        return latlng['lat'], latlng['lng']
    else:
        raise Exception("Nie znaleziono lokalizacji.")

def get_local_attractions(lat, lng, api_key, radius=5000):
    # pobieranie z api
    places_url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    params = {
        'location': f'{lat},{lng}',
        'radius': radius,
        'type': 'tourist_attraction',
        'key': api_key
    }
    response = requests.get(places_url, params=params).json()
    results = response.get('results', [])
    return [(place['name'], place.get('vicinity')) for place in results]

# 🔑 klucz API
API_KEY = "key"

# 🎯 Nazwa miejscowości
location_name = "Kraków, Polska"
#location_name = "Bydgoszcz, Polska"

lat, lng = get_place_coordinates(location_name, API_KEY)
attractions = get_local_attractions(lat, lng, API_KEY)
