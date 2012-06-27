import logging
import os

import pkgwat.api

import cliff.lister


class Search(cliff.lister.Lister):
    """ Show a list of packages that match a pattern.

    Remember, you can improve the search by tagging packages at
    http://apps.fedoraproject.org/tagger
    """

    log = logging.getLogger(__name__)

    def get_parser(self, prog_name):
        parser = super(Search, self).get_parser(prog_name)
        parser.add_argument('pattern')
        parser.add_argument('--rows-per-page', dest='rows_per_page', type=int, default=10)
        parser.add_argument('--start-row', dest='start_row', type=int, default=0)
        return parser

    def take_action(self, args):
        columns = ['name', 'summary']
        result = pkgwat.api.search(
            args.pattern,
            rows_per_page=args.rows_per_page,
            start_row=args.start_row,
        )
        rows = result['rows']
        return (
            columns,
            [[row[col] for col in columns] for row in rows],
        )
