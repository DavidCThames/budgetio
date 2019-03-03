import requests
import json
import csv
headers = {
    'Content-type': 'application/json',
    'user-key': '6205c2aca57feea920e875d2ca47078e'
}

data = '{"text":"Hello, World!"}'
latitudes = []
longitudes = []
names = []
with open('newDb.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            latitudes.append(row[1])
            longitudes.append(row[2])
            names.append(row[3])
            line_count += 1
# lat = str(47.668328)
# lon = str(-122.387233)
# response = requests.post('https://developers.zomato.com/api/v2.1/search?start=1&count=15&lat=' + lat + '&lon=' + lon + '&sort=rating&order=desc', headers=headers, data=data)
# print(response.json())
# with open("json1.json", "r") as read_file:
#     data = json.load(read_file)
# print(latitudes)
# print(longitudes)
# print(names)
neighborhoods = []
for i in range(len(latitudes)):
    aNeighborhood = {}
    aNeighborhood['latitude'] = latitudes[i]
    aNeighborhood['longitude'] = longitudes[i]
    aNeighborhood['name'] = names[i]
    lat = str(latitudes[i])
    lon = str(longitudes[i])
    response = requests.post('https://developers.zomato.com/api/v2.1/search?start=1&count=4&lat=' + lat + '&lon=' + lon + '&sort=real_distance&order=desc', headers=headers, data=data)
    data = response.json()
    restaurantNum = 1
    for val in data['restaurants']:
        rest = val['restaurant']
        tmp = {}
        tmp['name'] = rest['name']
        tmp['latitude'] = rest['location']['latitude']
        tmp['longitude'] = rest['location']['longitude']
        tmp['price_range'] = rest['price_range']
        tmp['user_rating'] = rest['user_rating']['aggregate_rating']
        tmp['photos_url'] = rest['photos_url']
        tmp['cuisines'] = rest['cuisines']
        tmp['has_online_delivery'] = rest['has_online_delivery']
        aNeighborhood['r' + str(restaurantNum)] = tmp
        restaurantNum += 1
    neighborhoods.append(aNeighborhood)
print(json.dumps(neighborhoods))
print(len(neighborhoods))
with open('seattle_restaurants.json', 'w') as outfile:
    json.dump(neighborhoods, outfile)