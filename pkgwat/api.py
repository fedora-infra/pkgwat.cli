
import collections
import json
import requests

import pkgwat.utils


BASE_URL = "https://apps.fedoraproject.org/packages/fcomm_connector"

koji_build_states = collections.OrderedDict((
    ('all', ''),
    ('building', '0'),
    ('success', '1'),
    ('failed', '3'),
    ('cancelled', '4'),
    ('deleted', '2'),
))


def _make_request(path, query, strip_tags):
    query_as_json = json.dumps(query)
    url = "/".join([BASE_URL, path, query_as_json])
    response = requests.get(url)
    d = json.loads(response.text)

    if strip_tags:
        d = pkgwat.utils.strip_tags(d)

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


def builds(package, state='all', rows_per_page=10,
             start_row=0, strip_tags=True):

    if state not in koji_build_states.values():
        state = koji_build_states[state]

    path = "koji/query/query_builds"
    query = {
        "filters": {
            "package": package,
            "state": state,
        },
        "rows_per_page": rows_per_page,
        "start_row": start_row,
    }

    return _make_request(path, query, strip_tags)
