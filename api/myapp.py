import requests
import json

URL = "http://127.0.0.1:8000/api/create/"

data = {
    'name': 'bikalpa',
    'roll_no': 3663,
    'address': 'ktm'
}

json_data = json.dumps(data)


r = requests.post(url = URL, data = json_data)

# data = r.json()
# print(data)
