import requests

API_KEY = "dcb4e4986e1ced3c56002e9554b76e49"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

GEOCODING_URL = "http://api.openweathermap.org/geo/1.0/direct"

city = input("Enter a city name: ")

requestCityLocation = f"{GEOCODING_URL}?q={city}&limit=1&appid={API_KEY}"

response = requests.get(requestCityLocation)

data = response.json()

print(data[0])
# request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
# response = requests.get(request_url)

# if response.status_code == 200:
# data = response.json()
# else:
#  print("An error occured")
