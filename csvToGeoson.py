import csv
import json
from collections import OrderedDict

li = []
with open('CurrentObs.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for latitude, longitude, weather, temp in reader:
        d = OrderedDict()
        d['type'] = 'Feature'
        d['geometry'] = {
            'type': 'Point',
            'coordinates': [float(latitude), float(longitude)]
        }
        d['properties'] = {
            'weather': weather,
            'temp': temp
        }
        li.append(d)

d = OrderedDict()
d['type'] = 'FeatureCollection'
d['features'] = li
with open('GeoObs.json', 'w') as f:
    f.write(json.dumps(d, sort_keys=False, indent=4))
