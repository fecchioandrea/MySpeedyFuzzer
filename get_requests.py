"""
Module useful in doing GET requests

"""

import concurrent.futures
import requests

MY_URL = ""


def download_site_get(code):
    """
        Makes the GET request for every single code
            and prints data in a formatted way.

        Args:
            code        -- the code to be used in the request

    """
    with requests.get(url=MY_URL.format(code.replace("/*", "%2f%2a"))) as response:
        print('{:30s} {:40s} {:90s}'.format(f'Read {len(response.content)} bytes with GET',
                                            f'using code: {code}',
                                            f'with status code: {response.content.status_code}')
              )


def download_all_sites_get(codes, num):
    """
        Initialises a ThreadPoolExecutor in order to make
            more asyncronous GET requests.

        Args:
            codes       -- list of codes

    """
    with concurrent.futures.ThreadPoolExecutor(max_workers=num) as executor:
        executor.map(download_site_get, codes)  # in "map" sta il ciclo


def make_get_requests(given_url, codes, num):
    """
        Initialises the GET requests.

        Args:
            given_url       -- the url given in the command-line
            codes           -- the list of codes to try
            num             -- the max number of threads to be used
    """
    global MY_URL
    MY_URL = given_url

    download_all_sites_get(codes, num)
