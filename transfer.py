import json

# Load the original JSON data
with open('seouldong.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Extract necessary information and create new features
new_features = []
for feature in data['features']:
    properties = feature['properties']
    adm_nm = properties['adm_nm']
    coordinates = properties['coordinates']

    new_feature = {
        'type': 'Feature',
        'geometry': {
            'type': 'Polygon',
            'coordinates': coordinates,
        },
        'properties': {
            'adm_nm': adm_nm,
        }
    }
    new_features.append(new_feature)

# Create a new GeoJSON FeatureCollection with the new features
new_data = {
    'type': 'FeatureCollection',
    'features': new_features
}

# Save the new GeoJSON data to a file
with open('Trans_seouldong.json', 'w', encoding='utf-8') as new_file:
    json.dump(new_data, new_file, ensure_ascii=False, indent=2)

print('Transformation and saving completed. Check Trans_seouldong.json')
