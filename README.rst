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

There is one.

>>> import pkgwat.api
>>> results = pkgwat.api.search("nethack")
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
      contents       Show contents of a package 
      help           print detailed help for another command
      info           Show details about a package 
      releases       List active releases for a package 
      search         Show a list of packages that match a pattern.
      updates        List bodhi updates for a package 

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

Overview info on a particular package::
    --- ~ » pkgwat info nethack
    +--------------+-------------------------------------------------------------------------+
    | Field        | Value                                                                   |
    +--------------+-------------------------------------------------------------------------+
    | upstream_url | http://nethack.org                                                      |
    | description  | NetHack is a single player dungeon exploration game that runs on a      |
    |              | wide variety of computer systems, with a variety of graphical and text  |
    |              | interfaces all using the same game engine.                              |
    |              |                                                                         |
    |              | Unlike many other Dungeons & Dragons-inspired games, the emphasis in    |
    |              | NetHack is on discovering the detail of the dungeon and not simply      |
    |              | killing everything in sight - in fact, killing everything in sight is   |
    |              | a good way to die quickly.                                              |
    |              |                                                                         |
    |              | Each game presents a different landscape - the random number generator  |
    |              | provides an essentially unlimited number of variations of the dungeon   |
    |              | and its denizens to be discovered by the player in one of a number of   |
    |              | characters: you can pick your race, your role, and your gender.         |
    | name         | nethack                                                                 |
    | summary      | A rogue-like single player dungeon exploration game                     |
    | link         | https://apps.fedoraproject.org/packages/nethack                         |
    | devel_owner  | lmacken                                                                 |
    +--------------+-------------------------------------------------------------------------+

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

License
-------

``pkgwat`` is licensed LGPLv2+.
