"""
Module useful in doing POST requests

"""

import concurrent.futures
import requests

MY_URL = ""
PARAM = {}


def split_data(par):
    """
        Splits the key and the value, in case they were indicated
            from the user in the command-line, to be used in POSTs.

        Args:
            par       -- parameters to be split

        Returns:
            couple      -- list of two separated elements (key and value)

    """
    couple = par.split('=')
    return [couple[0], couple[1]]


def download_site_post(code):
    """
        Makes the POST request for every single code
            and prints data in a formatted way.

        Args:
            code        -- the code to be used in the request

    """
    with requests.post(MY_URL, PARAM) as response:
        print('{:30s} {:40s} {:90s}'.format(f'Read {len(response.content)} bytes with POST',
                                            f'using code: {code}',
                                            f'giving status: {response.status_code}')
              )


def download_all_sites_post(codes, num):
    """
        Initialises a ThreadPoolExecutor in order to make
            more asyncronous POST requests.

        Args:
            codes       -- list of codes

    """
    with concurrent.futures.ThreadPoolExecutor(max_workers=num) as executor:
        executor.map(download_site_post, codes)  # in "map" sta il ciclo


def make_post_requests(data, given_url, codes, num):
    """
        Initialises the POST requests.

        Args:
            data            -- the dictionary with parameters
            given_url       -- the url given in the command-line
            codes           -- the list of codes to try
            num             -- the max number of threads to be used
    """
    data = split_data(data)

    global PARAM
    PARAM = {data[0]: data[1]}

    global MY_URL
    MY_URL = given_url

    download_all_sites_post(codes, num)
