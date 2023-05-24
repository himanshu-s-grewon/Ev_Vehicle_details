from utils import get_web_data, JSON_PATH
import json

ev_type = [4, 5, 6]


def get_maker(web_url):
    data_list = []
    for i in ev_type:
        data = {
            "data": i
        }
        data = get_web_data(web_url, data=data, post=True, formate='json')
        for x, dt in enumerate(data['value']):
            print(dt)
            maker_id = dt['id']
            maker_name = dt['name']
            ev_type_id = dt['ev_type_id']

            if dt['brand_images']:
                brand_logo = dt['brand_logo']
            else:
                brand_logo = None

            data_list.append({
                "ev_type_id": ev_type_id,
                "maker_id": maker_id,
                "maker_name": maker_name,
                "brand_logo": brand_logo
            })

    json_object = json.dumps(data_list, indent=2)

    # Writing to sample.json
    # with open(f"{JSON_PATH}/ev_vehicle_makers.json", "w") as outfile:
    #     outfile.write(json_object)
    return data_list
