import json
import requests
import time

parsed = []
with open('./fixtures/addresses.txt') as f:
    output = []
    rows = [l.replace('\n', '').split('     ') for l in f.readlines()]
    for i, row in enumerate(rows):

        result = requests.get(
            f'https://api.postcodes.io/postcodes/{row[1]}/').json()
        print(result['status'], i)
        skip = False
        while result['status'] != 200:
            if result['status'] == 404:
                skip = True
                break
            time.sleep(5)
            result = requests.get(
                f'https://api.postcodes.io/postcodes/{row[1]}/').json()

        if not skip:
            location = result['result']
            output.append(
                {
                    "model": "maps.Address",
                    "pk": i,
                    "fields": {
                        "postcode": row[1],
                        "name": row[0],
                        "latitude": location['latitude'],
                        "longitude": location['longitude'],
                    }
                }
            )

    with open('./fixtures/addresses.json', 'w') as out_file:
        json.dump(output, out_file)
