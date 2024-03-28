#!/usr/bin/python3
"""
This script takes GitHub credentials (username and personal access token) as arguments
and uses the GitHub API to display the user's id.
"""

import sys
import requests

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]

    url = 'https://api.github.com/user'
    response = requests.get(url, auth=(username, token))

    try:
        user_data = response.json()
        if 'id' in user_data:
            print(user_data['id'])
        else:
            print("None")
    except ValueError:
        print("None")
