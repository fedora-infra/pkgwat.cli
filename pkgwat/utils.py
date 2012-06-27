import six

try:
    # Python3
    from beautifulsoup4 import BeautifulSoup
except ImportError:
    from BeautifulSoup import BeautifulSoup


def strip_tags(d):
    """ Recursively strip XML tags from a dict, list, or string. """

    if type(d) == dict:
        return dict(((k, strip_tags(v)) for k, v in d.items()))

    if type(d) == list:
        return [strip_tags(element) for element in d]

    if isinstance(d, six.text_type):
        return BeautifulSoup(d).text

    return d
