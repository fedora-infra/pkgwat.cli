
import collections
import json
import requests

import pkgwat
import pkgwat.utils

import requests.defaults
requests.defaults.defaults['base_headers']['User-Agent'] = \
        'pkgwat/' + pkgwat.__version__


# TODO -- Tie this into cliff's verbosity options
DEBUG_REQUESTS = False
if DEBUG_REQUESTS:
    import sys

    class myobj(object):
        def write(self, message):
            print "DEBUG:", message

    requests.defaults.defaults['verbose'] = myobj()


BASE_URL = "https://apps.fedoraproject.org/packages/fcomm_connector"

koji_build_states = collections.OrderedDict((
    ('all', ''),
    ('building', '0'),
    ('success', '1'),
    ('failed', '3'),
    ('cancelled', '4'),
    ('deleted', '2'),
))

bodhi_releases = [
    "all",
    "f17",
    "f16",
    "f15",
    "el6",
    "el5",
]

bodhi_statuses = [
    "all",
    "stable",
    "testing",
    "pending",
    "obsolete",
]

yum_releases = [
    'Rawhide',
    'Fedora 16',
    'Fedora 16 Testing',
    'Fedora 15',
    'Fedora 15 Testing',
    'Fedora 14',
    'Fedora 14 Testing',
]

yum_arches = [
    'x86_64',
    'i686',
]

bugzilla_releases = collections.OrderedDict((
    ('all', ''),
    ('f17', '17'),
    ('f16', '16'),
    ('f15', '15'),
    ('el6', '6'),
    ('el5', '5'),
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


def updates(package, release="all", status="all", rows_per_page=10,
             start_row=0, strip_tags=True):

    if release not in bodhi_releases:
        raise ValueError("Invalid bodhi release. %r %r" % (
            release, bodhi_releases))

    if status not in bodhi_statuses:
        raise ValueError("Invalid bodhi status. %r %r" % (
            status, bodhi_statuses))

    if release == "all":
        release = ""

    if status == "all":
        status = ""

    path = "bodhi/query/query_updates"
    query = {
        "filters": {
            "package": package,
            "release": release,
            "status": status,
        },
        "rows_per_page": rows_per_page,
        "start_row": start_row,
    }

    return _make_request(path, query, strip_tags)


def bugs(package, release="all", rows_per_page=10, start_row=0, strip_tags=True):

    if release not in bugzilla_releases.values():
        release = bugzilla_releases[release]

    path = "bugzilla/query/query_bugs"
    query = {
        "filters": {
            "package": package,
            "version": release,
        },
        "rows_per_page": rows_per_page,
        "start_row": start_row,
    }

    return _make_request(path, query, strip_tags)


def contents(package, arch="x86_64", release="Rawhide", strip_tags=True):
    # This one behaves a little differently

    if release not in yum_releases:
        raise ValueError("Invalid yum release. %r %r" % (
            release, yum_releases))

    if arch not in yum_arches:
        raise ValueError("Invalid yum arch.  %r %r" % (
            arch, yum_arches))

    path = "yum/get_file_tree"
    query = {
        "package": package,
        "arch": arch,
        "repo": release,
    }
    url = "/".join([BASE_URL, path])
    response = requests.get(url, params=query)
    d = response.json

    if strip_tags:
        d = pkgwat.utils.strip_tags(d)

    return d


def changelog(package, rows_per_page=10, start_row=0, strip_tags=True):
    build_id = builds(package)['rows'][0]['build_id']

    path = "koji/query/query_changelogs"
    query = {
        "filters": {
            "build_id": build_id,
        },
        "rows_per_page": rows_per_page,
        "start_row": start_row,
    }

    return _make_request(path, query, strip_tags)
