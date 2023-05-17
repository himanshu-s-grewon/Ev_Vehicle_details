import json

from utils import get_web_data, JSON_PATH

four_wheelers_maker_id = ['4', '5', '16', '17', '18', '19', '21', '22', '23', '24', '39']
three_wheelers_maker_id = ['8', '9', '10', '11', '25', '26', '27', '28']
two_wheelers_maker_id = ['12', '13', '14', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38']


def get_ev_vehicle_model(web_url):
    data_list = []
    for i in four_wheelers_maker_id:
        data = {
            "data": i
        }
        data = get_web_data(web_url, data=data, post=True, formate='json')
        for x, dt in enumerate(data['value']):
            model_id = dt['id']
            model_name = dt['name']

            data_list.append({
                "ev_type_id": "4",
                "maker_id": i,
                "ev_model_id": model_id,
                "ev_model_name": model_name
            })

    for j in three_wheelers_maker_id:
        data = {
            "data": j
        }
        data = get_web_data(web_url, data=data, post=True, formate='json')
        for x, dt in enumerate(data['value']):
            model_id = dt['id']
            model_name = dt['name']

            data_list.append({
                "ev_type_id": "5",
                "maker_id": j,
                "ev_model_id": model_id,
                "ev_model_name": model_name
            })

    for m in two_wheelers_maker_id:
        data = {
            "data": m
        }
        data = get_web_data(web_url, data=data, post=True, formate='json')
        for x, dt in enumerate(data['value']):
            model_id = dt['id']
            model_name = dt['name']

            data_list.append({
                "ev_type_id": "6",
                "maker_id": m,
                "ev_model_id": model_id,
                "ev_model_name": model_name
            })

    json_object = json.dumps(data_list)

    # Writing to sample.json
    # with open(f"{JSON_PATH}/ev_vehicle_models.json", "w") as outfile:
    #     outfile.write(json_object)

    return data_list

