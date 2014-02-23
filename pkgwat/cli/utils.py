import datetime
import requests


def _format_time(timestamp):
    return datetime.datetime.fromtimestamp(timestamp).strftime("%Y/%m/%d")


def _format_link(link):
    if not link:
        return ''
    return requests.get('http://da.gd/s', params=dict(url=link)).text.strip()
