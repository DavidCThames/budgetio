import requests
import json
headers = {
    'Content-type': 'application/json',
    'user-key': '6205c2aca57feea920e875d2ca47078e'
}

data = '{"text":"Hello, World!"}'
latitudes = [47.668328,
47.614592,
47.538786,
47.62622,
47.724628,
47.615618,
47.607346,
47.643806,
47.558159,
47.60819,
47.656187,
47.564809,
47.679959,
47.694211,
47.628861,
47.649291,
47.680657,
47.62908,
47.66073,
47.622282,
47.658763,
47.636611
]
longitudes = [-122.387233,
-122.348464,
-122.275961,
-122.315979,
-122.287479,
-122.337897,
-122.335089,
-122.326777,
-122.378924,
-122.323829,
-122.352184,
-122.38585,
-122.333709,
-122.355289,
-122.354041,
-122.36301,
-122.313832,
-122.33685,
-122.305045,
-122.354226,
-122.334464,
-122.342938
]
# lat = str(47.668328)
# lon = str(-122.387233)
# response = requests.post('https://developers.zomato.com/api/v2.1/search?start=1&count=15&lat=' + lat + '&lon=' + lon + '&sort=rating&order=desc', headers=headers, data=data)
# print(response.json())
# with open("json1.json", "r") as read_file:
#     data = json.load(read_file)

restaurants = []
for i in range(len(latitudes)):
    lat = str(latitudes[i])
    lon = str(longitudes[i])
    response = requests.post('https://developers.zomato.com/api/v2.1/search?start=1&count=10&lat=' + lat + '&lon=' + lon, headers=headers, data=data)
    data = response.json()
    for val in data['restaurants']:
        rest = val['restaurant']
        tmp = {}
        tmp['name'] = rest['name']
        tmp['latitude'] = rest['location']['latitude']
        tmp['longitude'] = rest['location']['longitude']
        tmp['price_range'] = rest['price_range']
        tmp['user _rating'] = rest['user_rating']['aggregate_rating']
        tmp['photos_url'] = rest['photos_url']
        tmp['cuisines'] = rest['cuisines']
        tmp['has_online_delivery'] = rest['has_online_delivery']
        restaurants.append(tmp)
print(json.dumps(restaurants))
print(len(restaurants))
with open('seattle_restaurants.json', 'w') as outfile:
    json.dump(restaurants, outfile)