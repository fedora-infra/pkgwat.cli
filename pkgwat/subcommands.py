import logging

import pkgwat.api

import cliff.lister
import cliff.show


class Search(cliff.lister.Lister):
    """ Show a list of packages that match a pattern.

    You can improve the search by tagging packages at
    http://apps.fedoraproject.org/tagger
    """

    log = logging.getLogger(__name__)

    def get_parser(self, prog_name):
        parser = super(type(self), self).get_parser(prog_name)
        parser.add_argument('pattern')
        parser.add_argument('--rows-per-page', dest='rows_per_page',
                            type=int, default=10)
        parser.add_argument('--start-row', dest='start_row',
                            type=int, default=0)
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


class Info(cliff.show.ShowOne):
    """ Show details about a package """

    log = logging.getLogger(__name__)

    def get_parser(self, prog_name):
        parser = super(type(self), self).get_parser(prog_name)
        parser.add_argument('package')
        return parser

    def take_action(self, args):
        result = pkgwat.api.search(
            args.package,
            rows_per_page=1,
            start_row=0,
        )

        if not result['rows']:
            raise IndexError("No such package found.")

        package = result['rows'][0]

        package['link'] = "https://apps.fedoraproject.org/packages/%s" % \
                package['link']
        del package['sub_pkgs']  # TODO -- handle sub packages correctly.
        del package['icon']  # TODO -- use python-fabulous
        package['name'] = args.package

        return (package.keys(), package.values())


class Releases(cliff.lister.Lister):
    """ List active releases for a package """

    log = logging.getLogger(__name__)

    def get_parser(self, prog_name):
        parser = super(type(self), self).get_parser(prog_name)
        parser.add_argument('package')
        parser.add_argument('--rows-per-page', dest='rows_per_page',
                            type=int, default=10)
        parser.add_argument('--start-row', dest='start_row',
                            type=int, default=0)
        return parser

    def take_action(self, args):
        columns = ['release', 'stable_version', 'testing_version']
        result = pkgwat.api.releases(
            args.package,
            rows_per_page=args.rows_per_page,
            start_row=args.start_row,
        )
        rows = result['rows']
        return (
            columns,
            [[row[col] for col in columns] for row in rows],
        )


class Builds(cliff.lister.Lister):
    """ List active releases for a package """

    log = logging.getLogger(__name__)

    def get_parser(self, prog_name):
        parser = super(type(self), self).get_parser(prog_name)
        parser.add_argument('package')
        parser.add_argument('--state', dest='state', default='all',
                           help="One of %s" % (
                               ', '.join(pkgwat.api.koji_build_states)))
        parser.add_argument('--rows-per-page', dest='rows_per_page',
                            type=int, default=10)
        parser.add_argument('--start-row', dest='start_row',
                            type=int, default=0)
        return parser

    def take_action(self, args):
        columns = [
            'build id',
            'name-version-release',
            'state',
            'build time',
            'when',
            'owner',
        ]
        result = pkgwat.api.builds(
            args.package,
            args.state,
            rows_per_page=args.rows_per_page,
            start_row=args.start_row,
        )['rows']
        return (
            columns,
            [[
                build['build_id'],
                build['nvr'],
                build['state_str'],
                build['completion_time_display']['elapsed'],
                build['completion_time_display']['when'],
                build['owner_name'],
            ] for build in result]
        )
