from utils import get_web_data, JSON_PATH
import json


def get_ev_vehicle_type(web_url):
    data_list = []
    data = get_web_data(web_url, formate='json')

    for x, dt in enumerate(data['value']):
        ev_id = dt['id']
        ev_type_name = dt['name']

        data_list.append({
            "ev_id": ev_id,
            "ev_type_name": ev_type_name
        })

    json_object = json.dumps(data_list, indent=2)

    # Writing to sample.json
    with open(f"{JSON_PATH}/ev_vehicle_type.json", "w") as outfile:
        outfile.write(json_object)
