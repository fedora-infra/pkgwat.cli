import logging
import sys

import cliff.app
import cliff.commandmanager
from cliff.commandmanager import CommandManager

from pkgwat.cli import (
    __version__,
    __description__,
)


class PkgWat(cliff.app.App):

    log = logging.getLogger(__name__)

    def __init__(self):
        manager = cliff.commandmanager.CommandManager('pkgwat.subcommands')
        super(PkgWat, self).__init__(
            description=__description__,
            version=__version__,
            command_manager=manager,
        )

    def initialize_app(self, argv):
        self.log.debug('initialize_app')

    def prepare_to_run_command(self, cmd):
        self.log.debug('prepare_to_run_command %s', cmd.__class__.__name__)

    def clean_up(self, cmd, result, err):
        self.log.debug('clean_up %s', cmd.__class__.__name__)
        if err:
            self.log.debug('got an error: %s', err)


def main(argv=sys.argv[1:]):
    myapp = PkgWat()
    return myapp.run(argv)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
