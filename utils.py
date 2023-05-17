import requests
from requests.adapters import HTTPAdapter
from urllib3.util import Retry
import os
from pathlib import Path
from fake_useragent import UserAgent
import shutil

# Store all csv file here for local
ABS_PATH = Path(__file__).resolve().parent
JSON_PATH = os.path.join(ABS_PATH, 'output_files', 'json')


def get_web_data(url, post=False, data=dict, formate=None):
    # set headers
    ua = UserAgent()
    headers = {
        'user-agent': str(ua.random)
    }

    session = requests.Session()
    retry = Retry(connect=4, backoff_factor=2)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)

    # request for HTML document of given url
    if post:
        response = session.post(url, headers=headers, data=data)
    else:
        response = session.get(url, headers=headers, timeout=120)

    if formate == 'json':
        return response.json()
    return response.text
