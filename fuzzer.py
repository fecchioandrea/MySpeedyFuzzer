"""
Main module for the fuzzer.

Author: Andrea Fecchio, 2019
Computer Engineering degree - thesis work

"""

import sys
import threading
from parser import parse_args
from get_requests import make_get_requests
from post_requests import make_post_requests

THREAD_LOCAL = threading.local()


def build_list(files):
    """
        Build the Python list with codes to be used, starting
        from one or more text file(s) in which codes are listed.

        Args:
            files       -- list of inputfiles

        Returns:
            codes       -- list of codes to be used

    """
    codes = []
    for a_file in files:
        f_open = open(a_file, "r")
        lines = f_open.readlines()
        f_open.close()
        for line in lines:
            codes.append(line.replace("\n", ""))

    return codes


def main():
    """
    Main routine of the fuzzer.

    """
    args = parse_args(sys.argv[1:])
    num_threads = args.concurrency

    url = args.url

    codes = build_list(args.filelist)
    print("\n")

    if args.data is None:
        make_get_requests(url, codes, num_threads)
    else:
        make_post_requests(args.data, url, codes, num_threads)


if __name__ == '__main__':
    main()
