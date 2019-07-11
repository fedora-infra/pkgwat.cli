pkgwat
======

:Author: Ralph Bean <rbean@redhat.com>

.. comment: split here

Pronounced "package WAT".  ``pkgwat`` is a fast CLI tool for querying the
`fedora packages webapp <http://apps.fedoraproject.org/packages>`_.

You can make its search even better by `helping us tag packages
<http://apps.fedoraproject.org/tagger>`_.

Python API
----------

There is one.  You can download it indepenant of the CLI tools at
http://pypi.python.org/pypi/pkgwat.api

::

>>> from pkgwat import api
>>> results = api.search("nethack")
>>> results['rows'][0]['summary']
u'A rogue-like single player dungeon exploration game'

Shell Usage
-----------

Getting help::

    --- ~ » pkgwat --help
    usage: pkgwat [--version] [-v] [-q] [-h] [--debug]

    CLI tool for querying the fedora packages webapp

    optional arguments:
      --version      show program's version number and exit
      -v, --verbose  Increase verbosity of output. Can be repeated.
      -q, --quiet    suppress output except warnings and errors
      -h, --help     show this help message and exit
      --debug        show tracebacks on errors

    Commands:
      bugs           List bugs for a package
      builds         List koji builds for a package
      changelog      Show the changelog for a package
      complete       print bash completion command
      contents       Show contents of a package
      help           print detailed help for another command
      info           Show details about a package
      releases       List active releases for a package
      search         Show a list of packages that match a pattern.
      updates        List bodhi updates for a package
      dependencies   Show the dependencies for a package
      dependants     Show packages that dependent on a package
      provides       Show that which is provided by a given package
      obsoletes      Show that which is obsoleted by a given package
      conflicts      Show that which is marked as "conflict" by a given package

      To get the help of a command use "pkgwat help [command]".
You can enable activate bash completetion::

    $ pkgwat complete > pkgwat_complete.sh

    Add pkgwat_complete.sh in your .bashrc

    $ source .bashrc

    $ pkgwat
      bugs       changelog  contents   history    info       search
      builds     complete   help       icon       releases   updates

You can search for packages::

    --- ~ » pkgwat search nethack
    +------------------+-------------------------------------------------------+
    | name             | summary                                               |
    +------------------+-------------------------------------------------------+
    | nethack          | A rogue-like single player dungeon exploration game   |
    | nethack-vultures | NetHack- Vulture's Eye and Vulture's Claw             |
    | egoboo           | A top down graphical (3D) RPG in the spirit ofNethack |
    | slashem          | Super Lotsa Added Stuff Hack - Extended Magic         |
    | crossfire        | Server for hosting crossfire games                    |
    | crossfire-client | Client for connecting to crossfire servers            |
    +------------------+-------------------------------------------------------+

Flexibility with output formats for all commands::

    --- ~ » pkgwat help changelog
    usage: pkgwat changelog [-h] [-f {csv,html,json,table,yaml}] [-c COLUMN]
                            [--quote {all,minimal,none,nonnumeric}]
                            [--rows-per-page ROWS_PER_PAGE]
                            [--start-row START_ROW]
                            package

    Show the changelog for a package

    positional arguments:
      package

    optional arguments:
      -h, --help            show this help message and exit
      --rows-per-page ROWS_PER_PAGE
      --start-row START_ROW

    output formatters:
      output formatter options

      -f {csv,html,json,table,yaml}, --format {csv,html,json,table,yaml}
                            the output format, defaults to table
      -c COLUMN, --column COLUMN
                            specify the column(s) to include, can be repeated

    CSV Formatter:
      --quote {all,minimal,none,nonnumeric}
                            when to include quotes, defaults to nonnumeric

There's even a shell.  Just run ``$ pkgwat``.

Setting up development environment
----------------------------------

Make sure you have ``virtualenv`` installed and create a new venv::

  $ virtualenv env
  $ source env/bin/activate
  $ pip install -e .

If you intend to work also on ``pkgwat.api``, install your local version::

  $ pip install -e /path/to/pkgwat.api

Running the test suite
----------------------

Make sure you have ``tox`` installed and run it (outside of any virtualenv)::

  $ tox

Cutting a new release
---------------------

In order to generate a list of changes to be placed into ``CHANGELOG.rst``, use
the following command (this example generates the log between ``0.11`` and
``HEAD`` refs)::

  git log --reverse --format=format:'- %s `%h <https://github.com/fedora-infra/pkgwat.cli/commit/%H>`_' 0.11..HEAD

License
-------

``pkgwat`` is licensed LGPLv2+.
