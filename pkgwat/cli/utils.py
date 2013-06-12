import datetime
import re
import requests


ur1_ca_regexp = re.compile(
    r'<p class="success">Your ur1 is: '
    '<a href="(?P<shorturl>.+)">(?P=shorturl)</a></p>')


def _format_time(timestamp):
    return datetime.datetime.fromtimestamp(timestamp).strftime("%Y/%m/%d")


def _format_link(link):
    response = requests.post("http://ur1.ca/", data=dict(longurl=link))
    return ur1_ca_regexp.search(response.text).groupdict()['shorturl']
