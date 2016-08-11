import logging
import sys
import codecs
import locale

import pkg_resources

import cliff.app
import cliff.commandmanager
from cliff.commandmanager import CommandManager
# TODO -- how do we dynamically link these with setup.py?
__version__ = pkg_resources.get_distribution('pkgwat.cli').version
__description__ = "CLI tool for querying the fedora packages webapp"

requests_log = logging.getLogger("requests")
requests_log.setLevel(logging.WARN)


class PkgWat(cliff.app.App):

    log = logging.getLogger(__name__)

    def __init__(self):
        manager = cliff.commandmanager.CommandManager('pkgwat.subcommands')
        super(PkgWat, self).__init__(
            description=__description__,
            version=__version__,
            command_manager=manager,
            stdout=codecs.getwriter(locale.getpreferredencoding())(sys.stdout),
            stderr=codecs.getwriter(locale.getpreferredencoding())(sys.stderr),
        )

    def initialize_app(self, argv):
        self.log.debug('initialize_app')

    def prepare_to_run_command(self, cmd):
        self.log.debug('prepare_to_run_command %s', cmd.__class__.__name__)

    def clean_up(self, cmd, result, err):
        self.log.debug('clean_up %s', cmd.__class__.__name__)
        if err:
            self.log.debug('got an error: %s', err)

    # Overload run_subcommand to gracefully handle unknown commands.
    def run_subcommand(self, argv):
        try:
            self.command_manager.find_command(argv)
        except ValueError as e:
            if "Unknown command" in str(e):
                print("%r is an unknown command" % ' '.join(argv))
                print("Defaulting to 'info %s'" % ' '.join(argv))
                return super(PkgWat, self).run_subcommand(['info'] + argv)
            else:
                raise

        return super(PkgWat, self).run_subcommand(argv)


def main(argv=sys.argv[1:]):
    myapp = PkgWat()
    return myapp.run(argv)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
