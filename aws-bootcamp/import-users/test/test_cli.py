from import_users.cli import parse_args


def test_parse_args_with_all_arguments():
    args = ["--in", "data.csv", "--out", "creds.csv", "--log", "log.txt"]
    parsed_args = parse_args(args)
    assert parsed_args.infile == "data.csv"
    assert parsed_args.outfile == "creds.csv"
    assert parsed_args.logfile == "log.txt"


def test_parse_args_with_no_arguments():
    """Test parsing with no arguments should raise SystemExit"""
    import pytest

    with pytest.raises(SystemExit):
        parse_args([])
