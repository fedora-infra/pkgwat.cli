import pkgwat.cli.utils

def test_format_time():
    assert pkgwat.cli.utils._format_time(0) == "1970/01/01"
