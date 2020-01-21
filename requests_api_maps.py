import requests 

URL = "http://maps.googleapis.com/maps/api/geocode/json"
location = "Avenida Paulista"

PARAMS = {'address': location}

r = requests.get(url = URL, params = PARAMS)

data = r.json()
print (data)