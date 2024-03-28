#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL and displays
the value of the X-Request-Id variable found in the header of the response.
"""

import sys
import urllib.request

def display_request_id(url):
    """
    Fetches the URL and displays the value of the X-Request-Id variable
    found in the header of the response.

    Args:
        url (str): The URL to send the request to.
    """
    with urllib.request.urlopen(url) as response:
        request_id = response.getheader('X-Request-Id')
        print(request_id)

if __name__ == "__main__":
    url = sys.argv[1]
    display_request_id(url)
