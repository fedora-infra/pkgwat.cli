import six

from six.moves import html_parser


class MLStripper(html_parser.HTMLParser):
    strict = False
    def __init__(self):
        self.reset()
        self.fed = []

    def handle_data(self, d):
        self.fed.append(d)

    def get_data(self):
        return ''.join(self.fed)


def strip_tags(d):
    """ Recursively strip XML tags from a dict, list, or string. """

    if type(d) == dict:
        return dict(((k, strip_tags(v)) for k, v in d.items()))

    if type(d) == list:
        return [strip_tags(element) for element in d]

    if isinstance(d, six.text_type):
        s = MLStripper()
        s.feed(d)
        return s.get_data()

    return d
