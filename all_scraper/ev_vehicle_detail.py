import json

from utils import get_web_data, JSON_PATH

data_list = []


def ev_vehicle_detail(web_url, ev_detail_list):
    for ev_detail in ev_detail_list:
        _ev_deatil = {'ev1': ev_detail['ev_type_id'], 'make1': ev_detail['maker_id'],
                      'model1': ev_detail['ev_model_id']}

        data = {'data': f'{json.dumps(_ev_deatil)}'}
        _data = get_web_data(web_url, data=data, post=True, formate='json')
        for x, dt in enumerate(_data['value']):
            data_list.append(
                {
                    "maker_id": dt['maker_id'],
                    "makers": dt['makers'],
                    "model_id": dt['model_id'],
                    "model_name": dt['model_name'],
                    "battery": dt['battery'],
                    "battery_type": dt['battery_type'],
                    "price": dt['price'],
                    "image": dt['logopath'],
                    "distance_range": dt['distance_range'],
                    "charger_rating": dt['charger_rating'],
                    "charge_time": dt['charge_time']
                }
            )

    json_object = json.dumps(data_list)

    # Writing to sample.json
    # with open(f"{JSON_PATH}/ev_vehicle_all_details.json", "w") as outfile:
    #     outfile.write(json_object)