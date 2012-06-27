
import json
import requests

import utils


BASE_URL = "https://apps.fedoraproject.org/packages/fcomm_connector"


def _make_request(path, query, strip_tags):
    query_as_json = json.dumps(query)
    url = "/".join([BASE_URL, path, query_as_json])
    response = requests.get(url)
    d = json.loads(response.text)

    if strip_tags:
        d = utils.strip_tags(d)

    return d


def search(pattern, rows_per_page=10, start_row=0, strip_tags=True):
    path = "xapian/query/search_packages"
    query = {
        "filters": {"search": pattern},
        "rows_per_page": rows_per_page,
        "start_row": start_row,
    }

    return _make_request(path, query, strip_tags)


def releases(package, rows_per_page=10, start_row=0, strip_tags=True):
    path = "bodhi/query/query_active_releases"
    query = {
        "filters": {"package": package},
        "rows_per_page": rows_per_page,
        "start_row": start_row,
    }

    return _make_request(path, query, strip_tags)
