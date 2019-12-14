"""
Command Line Parsing Module

"""

import argparse


def parse_args(args):
    """
    This function parses the arguments which have been passed from the command
    line, these can be easily retrieved for example by using "sys.argv[1:]".
    It returns a parser object as with 'argparse'.

    Arguments:
        args        -- the list of arguments passed from the command line
                            as the sys.argv format

    Returns:
        parser      -- a parser with the provided arguments, which
                            can be used in a simpler format
    """
    parser = argparse.ArgumentParser(
        prog='PROG_NAME',
        description='Process the number of threads, the list of payloads and '
                    'the url for the authomatic multithreading fuzzing program.'
    )

    parser.add_argument(
        "-u", "--url",
        help="the url of the web app to be tested, with \"{}\" for payload (if GET)",
        type=str,
        required=True
    )
    parser.add_argument(
        "-t", "--concurrency",
        help="number of concurrent http requests",
        type=int,
        required=True
    )
    parser.add_argument(
        "-l", "--filelist",
        help="input .txt file(s), containing one payload per line",
        nargs='+',
        required=True
    )
    parser.add_argument(
        "-d", "--data",
        help="key-value couple (indicated: \"key={}\") staying for the parameter to be found (if POST)",
        type=str,
        required=False,
    )

    return parser.parse_args(args)
