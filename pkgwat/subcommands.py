import logging
import sys

import pkgwat.api

import cliff.lister
import cliff.show


class FCommLister(cliff.lister.Lister):
    """ Base Lister for fcomm_connector aware commands. """

    def get_parser(self, prog_name):
        parser = super(FCommLister, self).get_parser(prog_name)
        parser.add_argument('package')
        parser.add_argument('--rows-per-page', dest='rows_per_page',
                            type=int, default=37)
        parser.add_argument('--start-row', dest='start_row',
                            type=int, default=0)
        return parser


class Search(FCommLister):
    """ Show a list of packages that match a pattern.

    You can improve the search by tagging packages at
    http://apps.fedoraproject.org/tagger
    """

    log = logging.getLogger(__name__)

    def take_action(self, args):
        columns = ['name', 'summary']
        result = pkgwat.api.search(
            args.package,
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


class Releases(FCommLister):
    """ List active releases for a package """

    log = logging.getLogger(__name__)

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


class Builds(FCommLister):
    """ List koji builds for a package """

    log = logging.getLogger(__name__)

    def get_parser(self, prog_name):
        parser = super(type(self), self).get_parser(prog_name)
        parser.add_argument('--state', dest='state', default='all',
                           help="One of %s" % (
                               ', '.join(pkgwat.api.koji_build_states)))
        return parser

    def take_action(self, args):
        columns = ['build id', 'name-version-release', 'state',
                   'build time', 'when', 'owner']
        result = pkgwat.api.builds(
            args.package,
            args.state,
            rows_per_page=args.rows_per_page,
            start_row=args.start_row,
        )
        rows = result['rows']
        return (
            columns,
            [[
                build['build_id'],
                build['nvr'],
                build['state_str'],
                build['completion_time_display']['elapsed'],
                build['completion_time_display']['when'],
                build['owner_name'],
            ] for build in rows]
        )


class Updates(FCommLister):
    """ List bodhi updates for a package """

    log = logging.getLogger(__name__)

    def get_parser(self, prog_name):
        parser = super(type(self), self).get_parser(prog_name)
        parser.add_argument('--release', dest='release', default='all',
                           help="One of %s" % (
                               ', '.join(pkgwat.api.bodhi_releases)))
        parser.add_argument('--state', dest='status', default='all',
                           help="One of %s" % (
                               ', '.join(pkgwat.api.bodhi_statuses)))
        return parser

    def take_action(self, args):
        columns = ['id', 'status', 'karma', 'submitted', 'pushed']
        result = pkgwat.api.updates(
            args.package,
            status=args.status,
            release=args.release,
            rows_per_page=args.rows_per_page,
            start_row=args.start_row,
        )
        rows = result['rows']
        return (
            columns,
            [[
                update['id'],
                update['status'],
                update['karma_str'] + ", " + update['karma_level'],
                update['date_submitted_display'],
                update['date_pushed_display'],
            ] for update in rows]
        )


class Bugs(FCommLister):
    """ List bugs for a package """

    log = logging.getLogger(__name__)

    def get_parser(self, prog_name):
        parser = super(type(self), self).get_parser(prog_name)
        parser.add_argument('--release', dest='release', default='all',
                           help="One of %s" % (
                               ', '.join(pkgwat.api.bugzilla_releases)))
        return parser

    def take_action(self, args):
        columns = ['id', 'description', 'status', 'release']
        result = pkgwat.api.bugs(
            args.package,
            release=args.release,
            rows_per_page=args.rows_per_page,
            start_row=args.start_row,
        )
        rows = result['rows']
        return (
            columns,
            [[row[col] for col in columns] for row in rows],
        )


class Contents(cliff.command.Command):
    """ Show contents of a package """

    log = logging.getLogger(__name__)

    def get_parser(self, prog_name):
        parser = super(type(self), self).get_parser(prog_name)
        parser.add_argument('--arch', dest='arch', default='x86_64',
                            help="One of %s" % (
                                ', '.join(pkgwat.api.yum_arches)))
        parser.add_argument('--release', dest='release', default='Rawhide',
                            help="One of %s" % (
                                ', '.join(pkgwat.api.yum_releases)))
        return parser

    def take_action(self, args):
        result = pkgwat.api.contents(
            args.package,
            arch=args.arch,
            release=args.release,
        )
        self._recursive_print(result)
        sys.exit(0)

    def _recursive_print(self, d, prefix='/'):
        if type(d) == list:
            [self._recursive_print(element) for element in d]

        if type(d) == dict:
            filename = prefix + d['data']['title']
            if 'children' not in d:
                sys.stdout.write(filename + "\n")
            for child in d.get('children', []):
                self._recursive_print(child, prefix=filename + '/')


class Changelog(FCommLister):
    """ Show the changelog for a package """

    log = logging.getLogger(__name__)

    def take_action(self, args):
        columns = ['display_date', 'author', 'version', 'text']
        result = pkgwat.api.changelog(
            args.package,
            rows_per_page=args.rows_per_page,
            start_row=args.start_row,
        )
        rows = result['rows']
        return (
            columns,
            [[row[col] for col in columns] for row in rows],
        )
