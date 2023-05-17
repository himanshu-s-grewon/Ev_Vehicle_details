from all_scraper.ev_vehicle_detail import ev_vehicle_detail
from all_scraper.get_ev_vehicle_model import get_ev_vehicle_model
from all_scraper.get_ev_vehicle_type import get_ev_vehicle_type
from all_scraper.get_maker import get_maker
from web_urls import EV_VEHICLE_TYPE, MAKER, EV_VEHICLE_DETAIL, VEHICLE_MODEL


def bulk_scraper():
    # get_ev_vehicle_type(EV_VEHICLE_TYPE)
    # get_maker(MAKER)
    ev_detail_list = get_ev_vehicle_model(VEHICLE_MODEL)
    ev_vehicle_detail(EV_VEHICLE_DETAIL,ev_detail_list)


if __name__ == '__main__':
    bulk_scraper()
