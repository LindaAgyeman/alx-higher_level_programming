#!/usr/bin/python3
"""
Script that sends a POST request with an email as a parameter
and displays the body of the response (decoded in utf-8).
"""

import sys
import urllib.parse
import urllib.request

def post_email(url, email):
    """
    Sends a POST request to the specified URL with the email as a parameter.

    Args:
        url (str): The URL to send the POST request to.
        email (str): The email to include in the request.

    Returns:
        str: The response body of the request.
    """
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    req = urllib.request.Request(url, data=data, method='POST')

    with urllib.request.urlopen(req) as response:
        body = response.read().decode('utf-8')
        return body

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    response_body = post_email(url, email)
    print("Your email is:", response_body)
