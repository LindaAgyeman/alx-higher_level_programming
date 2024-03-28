#!/usr/bin/python3
"""
This script takes repository name and owner name as arguments
and uses the GitHub API to fetch and print the 10 most recent commits.
"""

import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./100-github_commits.py <repository_name> <owner_name>")
        sys.exit(1)

    repository_name = sys.argv[1]
    owner_name = sys.argv[2]

    url = f"https://api.github.com/repos/{owner_name}/{repository_name}/commits"
    response = requests.get(url)

    try:
        commits = response.json()
        for commit in commits[:10]:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")
    except ValueError:
        print("Failed to parse JSON response.")
        sys.exit(1)
