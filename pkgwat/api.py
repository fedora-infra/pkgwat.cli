
import json
import requests

import utils

BASE_URL = "https://apps.fedoraproject.org/packages/" + \
        "fcomm_connector/xapian/query/search_packages/"


def search(pattern, rows_per_page=10, start_row=0, strip_tags=True):
    query_params = {
        "filters": {"search": pattern},
        "rows_per_page": rows_per_page,
        "start_row": start_row,
    }

    query_as_json = json.dumps(query_params)
    URL = BASE_URL + query_as_json
    response = requests.get(URL)
    d = json.loads(response.text)

    if strip_tags:
        d = utils.strip_tags(d)

    return d
